import os
import shutil
from datetime import datetime
import psycopg2
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv

load_dotenv()  # loads the configs from .env

"""
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
https://developers.google.com/docs/api/quickstart/python
"""

class DatabaseCopier:
    def __init__(self, database_name, username, password, host, port):
        self.database_name = database_name
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    def connect_to_database(self):
        try:
            conn = psycopg2.connect(
                database=self.database_name,
                user=self.username,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return conn
        except psycopg2.Error as e:
            print("Error: Unable to connect to the database")
            print(e)
            return None

    def backup_database(self, output_dir):
        connection = self.connect_to_database()
        if connection:
            cursor = connection.cursor()
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_file = os.path.join(output_dir, f"{self.database_name}_{timestamp}.csv")
            try:
                # Create the 'backups' directory if it doesn't exist
                os.makedirs(output_dir, exist_ok=True)
                with open(backup_file, "w") as f:
                    cursor.copy_expert(f"COPY (SELECT * FROM information_schema.tables WHERE table_schema NOT IN ("
                                       f"'pg_catalog', 'information_schema')) TO STDOUT WITH CSV", f)
                print("Database backup completed successfully.")
                return backup_file
            except psycopg2.Error as e:
                print("Error: Unable to backup the database.")
                print(e)
            finally:
                cursor.close()
                connection.close()
        return None

    def import_data(self, csv_file):
        connection = self.connect_to_database()
        if connection:
            cursor = connection.cursor()
            try:
                with open(csv_file, "r") as f:
                    cursor.copy_expert(f"COPY {self.database_name} FROM STDIN WITH CSV HEADER", f)
                connection.commit()
                print("Data imported successfully.")
            except psycopg2.Error as e:
                connection.rollback()
                print("Error: Unable to import data into the database.")
                print(e)
            finally:
                cursor.close()
                connection.close()

class GoogleDriveUploader:
    def __init__(self, credentials_file_path):
        self.credentials_file_path = credentials_file_path

    def authenticate(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_file_path,
                scopes=["https://www.googleapis.com/auth/drive"]
            )
            drive_service = build('drive', 'v3', credentials=credentials)
            return drive_service
        except Exception as e:
            print("Error: Unable to authenticate Google Drive.")
            print(e)
            return None

    def upload_file(self, file_path, folder_id):
        drive_service = self.authenticate()
        if drive_service:
            try:
                file_metadata = {
                    'name': os.path.basename(file_path),
                    'parents': [folder_id]
                }
                media = MediaFileUpload(file_path, resumable=True)
                file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
                print(f"File uploaded successfully. File ID: {file.get('id')}")
                return True
            except Exception as e:
                print("Error: Unable to upload file to Google Drive.")
                print(e)
        return False

def run():
    # PostgreSQL database configuration
    db_config = {
        'database_name': os.getenv("SUPABASE_DB"),
        'username': os.getenv("SUPABASE_DB_USER"),
        'password': os.getenv("SUPABASE_DB_PASSWORD"),
        'host': os.getenv("SUPABASE_DB_HOST"),
        'port': os.getenv("SUPABASE_DB_PORT"),
    }

    # Google Drive credentials and folder ID
    credentials_file_path = 'google-drive-credentials.json'  # Path to your Google Drive credentials JSON file
    folder_id = '1xbKnVBgaKyFz8Vpe3bkc5AwqYhIdmb4B'  # ID of the folder in Google Drive where you want to upload the backups

    # Directory to store the backups
    backup_output_dir = 'backups'

    # Create database copier object
    db_copier = DatabaseCopier(**db_config)

    # Backup the database
    backup_file = db_copier.backup_database(backup_output_dir)

    if backup_file:
        # Create Google Drive uploader object
        drive_uploader = GoogleDriveUploader(credentials_file_path)

        # Upload backup file to Google Drive
        drive_uploader.upload_file(backup_file, folder_id)

        # Clean up backup directory
        shutil.rmtree(backup_output_dir)

if __name__ == "__main__":
    run()