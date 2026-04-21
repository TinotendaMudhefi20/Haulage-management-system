FINAL README 
# Haulage Truck Management System

## Overview

This project is a full-stack Haulage Truck Management System designed to simulate basic logistics operations.

The system allows users to manage trucks, drivers, and delivery jobs. It also enforces real-world business rules, such as preventing a driver or truck from being assigned to multiple active jobs at the same time.

A REST API was built using Django REST Framework, and a simple user interface was developed using React so that the system can be tested through a real user experience, not just API tools.

The backend is containerized using Docker, while the frontend runs separately in a development environment.

The project also includes:
- Token-based authentication for securing API access
- Swagger UI for interactive API documentation and testing

---

## Features

- Truck management (create, view, update, delete)
- Driver management (create, view, update, delete)
- Job management (create, view, update, delete)
- Business rule enforcement (no double assignment of drivers or trucks)
- Token-based authentication
- Swagger API documentation
- React frontend for user interaction
- Dockerized backend with PostgreSQL database

---

## Technology Stack

Backend:
- Django
- Django REST Framework
- PostgreSQL

Frontend:
- React
- Bootstrap

Other Tools:
- Docker
- Swagger (drf-yasg)

---

## How to Run the Project

### 1. Run the Backend (Docker)

Make sure Docker is installed and running.

From the project root directory, run:


docker-compose up --build


This will start:
- Django backend
- PostgreSQL database

Once running:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/swagger/
- Admin panel: http://127.0.0.1:8000/admin/

---

### 2. Create a Superuser (Admin Access)

To access the Django admin panel, create a superuser:


docker-compose exec web python manage.py createsuperuser


Follow the prompts to set:
- username
- email
- password

Then log in at:

http://127.0.0.1:8000/admin/

---

### 3. Create an Authentication Token

To generate a token for API authentication:


docker-compose exec web python manage.py drf_create_token <username>


Example:


docker-compose exec web python manage.py drf_create_token admin


This will return a token like:


Generated token: abc123...


You can use this token in API requests:


Authorization: Token abc123...


---

### 4. Run the Frontend (React)

Open a new terminal and run:


cd frontend
npm install
npm start


The frontend will run at:

http://localhost:3000

---

## How Authentication Works

The system supports token-based authentication.

- A user logs in (via admin or system)
- A token is generated for that user
- The token is included in API requests to identify the user

Although the backend supports authentication, the frontend currently runs without enforcing login for simplicity during testing.

---

## Using Swagger (API Testing)

Swagger UI provides an easy way to test the API without using external tools.

Visit:

http://127.0.0.1:8000/swagger/

You can:
- View all endpoints
- Send requests
- Test responses

If authentication is required, click "Authorize" and enter:


Token your_token_here


---

## Notes

- The frontend is not containerized and runs separately.
- The backend enforces business rules such as preventing multiple active job assignments.
- Error handling is implemented in the frontend to display meaningful messages.
- Pagination is implemented at the API level.

---

## Conclusion

This project demonstrates a full-stack system with a focus on backend logic, API design, and real-world constraints, while also providing a simple frontend interface for usability and testing.
