# Restaurant Management System

![Restaurant Management System](https://via.placeholder.com/800x400.png?text=Restaurant+Management+System)

## Overview

Welcome to the **Restaurant Management System API**! This project is a robust restaurant management system built using **Django** and **Django REST Framework (DRF)**. It provides functionalities for managing restaurant operations, rate limiting, including **user authentication, inventory management, menu handling, order processing, table reservations, reporting, and analytics**.

Additionally, the project includes **test coverage analysis using Coverage.py**, ensuring that at least **90%** of the codebase is covered by unit tests written with **pytest**.

---

## Features

### **User Authentication**
- **JWT Authentication**: Secure authentication using **Djoser** and JSON Web Tokens (JWT).
- **Custom User Model**: Extended user model with additional fields and permissions.

### **Inventory Management**
- **Add, Update, Delete Inventory Items**: Manage stock levels of ingredients and supplies.
- **Low Stock Alerts**: Notify when an item is running low.
- **Track Inventory Usage**: Monitor ingredient consumption based on menu orders.

### **Menu Management**
- **Create, Update, Delete Menu Items**: Full CRUD operations for restaurant menus.
- **Categorized Menu**: Organize menu items into categories like appetizers, mains, and desserts.
- **Pricing and Availability**: Set prices and manage availability of dishes.

### **Order Processing**
- **Create and Manage Orders**: Customers can place orders.
- **Order Status Updates**: Track orders from preparation to delivery.
- **Calculate Total Bill**: Generate customer bills including tax and service charges.

### **Table Reservations**
- **Reserve Tables**: Customers can book tables in advance.
- **Cancel Reservations**: Easy cancellation and modification of bookings.
- **Seating Arrangement Optimization**: Efficient table allocation.

### **Reporting and Analytics**
- **Sales Reports**: Track revenue and order statistics.
- **Inventory Reports**: Monitor stock usage and waste.
- **Customer Insights**: Understand ordering trends and preferences.

### **Testing and Coverage**
- **Unit Tests**: Comprehensive tests for all functionalities using **pytest**.
- **Coverage Analysis**: Uses **Coverage.py** to measure test coverage, ensuring **90%+** code coverage.

---

## Installation

### **Prerequisites**
- Python 3.8+
- PostgreSQL
- Django 5.1.6

### **Setup**

#### **1. Clone the Repository**
```sh
git clone https://github.com/Andrew-oduola/restaurant_management_api.git
cd restaurant_management_api
```

#### **2. Create a Virtual Environment and Activate It**
```sh
python -m venv venv
# Activate virtual environment
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

#### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

#### **4. Set Up Environment Variables**
Create a `.env` file in the project root and add the following:
```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

#### **5. Run Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

#### **6. Create a Superuser**
```sh
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

#### **7. Run the Development Server**
```sh
python manage.py runserver
```
Access the application at: **http://127.0.0.1:8000/**

---

## API Endpoints

### **Authentication**
- **Login:** `POST /auth/jwt/create/`
- **Refresh Token:** `POST /auth/jwt/refresh/`
- **Verify Token:** `POST /auth/jwt/verify/`

### **Inventory**
- **List Items:** `GET /api/inventory/`
- **Create Item:** `POST /api/inventory/`
- **Retrieve Item:** `GET /api/inventory/{id}/`
- **Update Item:** `PUT /api/inventory/{id}/`
- **Delete Item:** `DELETE /api/inventory/{id}/`

### **Menu**
- **List Menu Items:** `GET /api/menu/`
- **Create Menu Item:** `POST /api/menu/`
- **Retrieve Menu Item:** `GET /api/menu/{id}/`
- **Update Menu Item:** `PUT /api/menu/{id}/`
- **Delete Menu Item:** `DELETE /api/menu/{id}/`

### **Orders**
- **List Orders:** `GET /api/orders/`
- **Create Order:** `POST /api/orders/`
- **Retrieve Order:** `GET /api/orders/{id}/`
- **Update Order:** `PUT /api/orders/{id}/`
- **Delete Order:** `DELETE /api/orders/{id}/`

### **Reservations**
- **List Reservations:** `GET /api/reservations/`
- **Create Reservation:** `POST /api/reservations/`
- **Retrieve Reservation:** `GET /api/reservations/{id}/`
- **Update Reservation:** `PUT /api/reservations/{id}/`
- **Delete Reservation:** `DELETE /api/reservations/{id}/`

### **Tables**
- **List Tables:** `GET /api/tables/`
- **Create Table:** `POST /api/tables/`
- **Retrieve Table:** `GET /api/tables/{id}/`
- **Update Table:** `PUT /api/tables/{id}/`
- **Delete Table:** `DELETE /api/tables/{id}/`

---

## Running Tests and Coverage Analysis

### **Install and Set Up Pytest & Coverage**
```sh
pip install pytest pytest-django coverage
```

### **Run Pytest**
```sh
pytest
```

### **Measure Test Coverage**
```sh
coverage run -m pytest
coverage report -m
```
Ensure that test coverage is at least **90%**.

### **Generate HTML Coverage Report**
```sh
coverage html
```
Open `htmlcov/index.html` in a browser to view detailed coverage analysis.

---

## Project Structure
```
📂 restaurant_management
│── 📁 customusers       # User authentication and management
│── 📁 inventory         # Inventory management
│── 📁 menu             # Menu-related models, views, serializers
│── 📁 orders           # Order processing
│── 📁 reporting        # Reporting and analytics
│── 📁 reservations     # Table reservations
│── 📁 tables           # Table management
│── 📁 restaurant_management  # Main project file
│── 📄 manage.py        # Django project manager
│── 📄 requirements.txt # Dependencies
│── 📄 .env             # Environment variables
│── 📄 README.md        # Project documentation
│── 📄 .gitattributes
│── 📄 .gitignore
│── 📄 pytest.ini
```

---

Happy Coding! 🚀

