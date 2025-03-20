
# Student Management System

This project is a web-based Student Management System built using Python Django and MySQL. It allows administrators to manage student details, including personal information, marks, and scores. The application also uses Postman for API testing and development.


## Features

- Student Management: Add, update, and delete student information.
- Marks and Scores: Manage and store students' marks and scores for various subjects.
- Database Integration: MySQL is used to securely store and retrieve data.
- API Support: APIs are built using Django REST framework and tested with Postman for seamless integration.


## Installation

Create and activate a virtual environment:

python -m venv env
source env/bin/activate 
Install the required dependencies:

pip install -r requirements.txt
Set up the database:

Create a MySQL database and update the database configuration in settings.py.
Apply migrations:

python manage.py makemigrations
python manage.py migrate
Run the development server:

python manage.py runserver
    
## API Reference

The project includes APIs for managing student data. Use Postman or any API client to interact with these endpoints.

Example Endpoints

Retrieve All Students: GET /api/students/
Retrieve a Specific Student: GET /api/students/<id>/
Add a New Student: POST /api/students/
Update Student Details: PUT /api/students/<id>/
Delete a Student: DELETE /api/students/<id>/
API Testing with Postman:

Import the provided Postman collection (if available) to quickly test all available APIs.
Ensure the server is running while using Postman


## Tech Stack

- Backend: Python Django
- Database: MySQL
- API Development and Testing: Django REST framework, Postman


## user input

Score Table:
   - Input: `mark`, `grade`

Student Details Table:

   - Input: `name`, `roll number`, `standard`, `gender`, `date of birth`

   Mark Table:
   - Input: `subject`, `mark`

   Personal Table:
   - Input: `parent name`, `address`, `phone number`
