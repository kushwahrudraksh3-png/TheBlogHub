# Django Blog Application

A modern and responsive Blog Application built using Django, Bootstrap, HTML, CSS and MySQL.

This project includes a custom admin panel with Role Based Access Control (RBAC) using Django Groups and Permissions.

Users are divided into different roles such as Admin, Editor and Normal User.  
Each role has different access permissions and dashboard functionality.

---

# Features

## Authentication System

- User Registration
- User Login
- User Logout
- Secure Authentication System

---

## Blog Features

- Create Blog Posts
- Update Blog Posts
- Delete Blog Posts
- View Blog Details
- Featured Blogs
- Blog Categories
- Blog Search Functionality
- Recent Posts Section

---

## Comment System

- Add Comments on Blogs
- Comment Management

---

## Custom Admin Panel

- Separate Custom Dashboard
- Beautiful Admin Interface
- Sidebar Navigation
- User Management
- Category Management
- Blog Management

---

## Role Based Access Control (RBAC)

This project uses Django Groups and Permissions for access control.

### Admin

Admin has full access to the system.

#### Admin Permissions

- Manage Users
- Manage Editors
- Manage Blogs
- Manage Categories
- Assign Permissions
- Access Full Dashboard
- Delete Any Content

---

### Editor

Editors can manage blog-related content.

#### Editor Permissions

- Create Blogs
- Update Blogs
- Delete Their Blogs
- Access Editor Dashboard
- Manage Blog Content

---

### User

Normal users can use public features.

#### User Permissions

- Read Blogs
- Search Blogs
- Add Comments

---

# Technologies Used

## Backend

- Python
- Django

---

## Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

---

## Database

- MySQL

---

## Tools & Platforms

- Git
- GitHub
- VS Code
- Ubuntu Linux

---

# Project Structure

```bash
BLOG/
│
├── about_links/        # About and social links app
├── blog_main/          # Main project settings and configurations
├── blogs/              # Blog application
├── dashboards/         # Custom admin and editor dashboard
├── env/                # Virtual environment
├── media/              # Uploaded media files
├── templates/          # HTML templates
│
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

---

# Installation Guide

## 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

---

## 2. Go to Project Directory

```bash
cd your-repository-name
```

---

## 3. Create Virtual Environment

```bash
python -m venv env
```

---

## 4. Activate Virtual Environment

### Linux / Ubuntu

```bash
source env/bin/activate
```

### Windows

```bash
env\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Configure Database

Update database settings inside:

```bash
settings.py
```

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER': 'root',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 7. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 8. Create Superuser

```bash
python manage.py createsuperuser
```

---

## 9. Run Development Server

```bash
python manage.py runserver
```

---

# Screenshots

Add your project screenshots here.

Example:

- Home Page
- Blog Detail Page
- Custom Admin Dashboard
- Editor Dashboard
- Login Page

---

# Future Improvements

- Rich Text Editor
- Like and Bookmark System
- User Profile System
- Dark Mode
- Email Verification
- REST API Integration
- Notifications System

---

# Author

## Rudraksh Kushwah

B.Tech CSE Student  
Frontend & Django Developer

GitHub: https://github.com/kushwahrudraksh3-png

---

# License

This project is for learning and educational purposes.