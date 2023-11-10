# Web Dev Lab

### Features
 - Selling courses
 - Blog on http://blog.webdevlab.org
 - Create short tutorial
 - Create developer team (career opportunity)
 - Create most advanced User Authentication system (Cookie based)
 - Forum on http://forum.webdevlab.org
 - User role (Admin, Student, Viewer)
 - 

### Database Modeling (PostgresSQL)
 - Articles Table:
    - article_id (Primary Key)
    - title
    - content
    - publication_date
    - author_id (Foreign Key referencing the Authors Table)
    - category_id (Foreign Key referencing the Categories Table)

 - Authors Table:
    - author_id (Primary Key)
    - name
    - email
    - bio

 - Comments Table:
    - comment_id (Primary Key)
    - article_id (Foreign Key referencing the Articles Table)
    - author_name
    - email
    - comment_text
    - comment_date

 - Categories Table:
    - category_id (Primary Key)
    - name

 - Tags Table:
    - tag_id (Primary Key)
    - name

 - ArticleTags Table (a junction table to implement many-to-many relationship between Articles and Tags):
   - article_id (Foreign Key referencing the Articles Table)
   - tag_id (Foreign Key referencing the Tags Table)