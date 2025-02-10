# Django-Auth
# Django Authentication App

## Overview
This is a Django-based authentication system that allows users to sign up, log in, reset passwords, and access a protected dashboard. The project implements user authentication using Django's built-in authentication framework.

## Features
- User Registration
- User Login & Logout
- Password Reset via Email
- Protected Dashboard for Authenticated Users

## Tech Stack
- **Backend:** Django
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite (default)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/jatinsharma30/Django-Auth.git
   cd Django-Auth
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the root directory:
     ```
     EMAIL_HOST_USER=your_email@gmail.com
     EMAIL_HOST_PASSWORD=your_app_password
     ```
   - Ensure you are using an **App Password** for Gmail authentication.

5. Run migrations:
   ```sh
   python manage.py migrate
   ```
6. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
7. Start the server:
   ```sh
   python manage.py runserver
   ```

## Deployment (PythonAnywhere)
1. Upload your project to PythonAnywhere.
2. Ensure `.env` is correctly placed and loaded in `wsgi.py`.
3. Restart the web app from the PythonAnywhere dashboard.

## Hosted Link
You can access the live project here: [Django Auth App](https://jatinsharma30.pythonanywhere.com/)

## Troubleshooting
- **Password Reset Email Not Sending?**
  - Ensure `.env` is loaded correctly.
  - Use an **App Password** for Gmail SMTP.
  - Restart the web app after changes.

## Usage
- Visit the home page (`/`) to log in or sign up.
- Once logged in, access the protected dashboard.
- If you forget your password, use the password reset feature.

## License
This project is open-source and available under the MIT License.

## Author
Developed by **Jatin Sharma** 🚀

