# User Authentication

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MuhammedAnasEP/User-Authentication.git
   cd User-Authentication
   
2. Create a virtual environment and activate it:

   ```bash
     python -m venv venv Or virtualenv venv
     source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install dependencies:

   ```bash
     pip install -r requirements.txt

4. Connect Database:
   
     I used SQLite engin for database,
     if your using same you don't want to change anything.
     Or you want to connect with other engines like PostgreSQL, MySQL etc. You want to change the engine section and want to add username, password, name of the database, and host.

5. Run migrations:
 
   ```bash
    python manage.py makemigrations
    python manage.py migrate

  
7. Run the server:
    
   ```bash
    python manage.py runserver

## API Endpoints

  None: I used JWT Authentication in user and logout endpoint for secruty. And The token is stored in the HTTPOnly Cookie.Use Postman for the checking the api it will or other
        platforms. And send Token with every request.

    POST /api/auth/register: Register user for authentication
    POST /api/auth/login: Login user get token and store token to the cookies
    POST /api/auth/logout: Logout user and remove token from the cookies
    POST /api/auth/refresh-token: Create new token
    GET /api/auth/user: for fetch the data of current logined user
  

