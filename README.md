# Task Manager API

A simple Task Manager REST API built with Django and Django REST Framework.  
This project allows users to register, login using JWT authentication, and manage tasks with different roles (Admin and User).

---

## Environment Setup & Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/sanchitagurav/taskmanager_project.git
cd taskmanager_project
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
pip install -r requirements.txt

**Database & Server Setup**
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (admin)
python manage.py createsuperuser

# Run the development server
python manage.py runserver


**Register a User**

Endpoint: POST /api/auth/register/

Body (JSON):

{
  "username": "exampleuser",
  "password": "examplepassword"
}


Response: Newly created user details

**Obtain JWT Tokens (Login)**

Endpoint: POST /api/auth/login/

Body (JSON):

{
  "username": "exampleuser",
  "password": "examplepassword"
}


Response:

{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}


Refresh token endpoint: POST /api/auth/refresh/ with body:

{
  "refresh": "<refresh_token>"
}

**Using JWT Tokens in Requests
**
Include token in request headers:

Authorization: Bearer <access_token>


Example:

curl -H "Authorization: Bearer <access_token>" http://127.0.0.1:8000/api/tasks/

**Roles (Admin, User)**

Admin: Can manage all tasks and assign tasks to users.

User: Can only view and manage their own tasks.

Assign roles by creating user via Django admin or using is_staff field.
