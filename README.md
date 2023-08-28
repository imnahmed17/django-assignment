# Django Product Review Application

Welcome to the **Django Product Review Application!** This is a web application built using Django that allows users to view a list of products, see product details, and submit reviews for products. The application utilizes PostgreSQL as its database backend to store product and review data.

## Features

- **Product List View**: Users can browse through a list of available products.
- **Product Detail View**: Users can view detailed information about a specific product.
- **Review Submission**: Users can submit reviews for products, including a rating and written feedback.

## Prerequisites

- Python 
- Docker
- PostgreSQL / PGAdmin
- Django
- psycopg2-binary
- Pillow
- django-environ

## Installation

**1. Clone this repository:**
```bash
git clone https://github.com/imnahmed17/django-assignment.git
cd django-assignment
code .
```

**2. Create and activate virtual environment:**

Firstly, type `Ctrl+Shift+P`. Then select the **Python: Create Environment** command to create a virtual environment in your workspace. Select `venv` and then the Python environment you want to use to create it. After this, type `` Ctrl+Shift+` ``, which creates a terminal and automatically activates the virtual environment by running its activation script.

**3. Install the required dependencies:**

```bash
pip install -r requirement.txt
```

**4. PostgreSQL setup:**
```bash
cd pg
docker-compose up -d
```
Now open your browser and type `http://localhost:8080` into the url to access PostgreSQL. For login give Email: admin@user.com and Password: adminuser. After that, right click on `Server > Register > Server` in left sidemenu. In general tab give type any name you want as Server name. In connection tab give Host name: postgres, Username: myuser, Password: mypassword and save it. Then nevigate your server name and create a database right clicking on your server name.

**5. Environment variable setup:**

Create a `.env` file in the same directory where `settings.py` resides and add the following key-value pair inside the file.
```bash
DATABASE_NAME=db_name
DATABASE_USER=myuser
DATABASE_PASSWORD=mypassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

**6. Run this application:**
```bash
cd ..
cd ecommerce
python manage.py migrate
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
python manage.py runserver
```
Now, open a web browser and go to `http://127.0.0.1:8000/admin` to add some products. To see all added product go to `http://127.0.0.1:8000/products`.