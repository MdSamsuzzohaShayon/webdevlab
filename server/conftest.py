import os
import django
from django.conf import settings
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


# Load test environment variables
dotenv_path = os.path.join(BASE_DIR, '.env.test')
load_dotenv(dotenv_path)