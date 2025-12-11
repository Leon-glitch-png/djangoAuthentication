# Simple Django Authentication Website

A minimal, secure, and easy-to-run Django application that implements user authentication (signup, login, logout, password reset), user profile, and a small protected dashboard. 


# 1. Installation

Clone the repository and set up a Python virtual environment:

```bash
git clone https://github.com/Leon-glitch-png/djangoAuthentication.git
cd djangoAuthentication

# Create virtual environment (recommended)
python -m venv .venv
# Activate:
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Windows (cmd)
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```


---

# 2. Features

* User registration (signup) with email and password
* User login and logout
* Password reset via email (console backend by default)
* Simple, responsive UI built with Tailwind / daisyUI (configurable)

---
---


# 3. Configuration (`.env`)

Create a `.env` file in the project root . Example:

```
SECRET_KEY="sample_key"
DEBUG='True'


# Database 
# For MySQL / Docker see next section:
DB_ENGINE='django.db.backends.mysql'
DATABASE_NAME='mydb'
MYSQL_USER='myuser'
MYSQL_PASSWORD='mypassword'
HOST='localhost'
PORT='3306'

# Email (for password reset)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = 'True'
EMAIL_HOST_USER = 'sample@gmail.com'
EMAIL_HOST_PASSWORD = 'your_gmail_app_password'

```

The project should load these values using `python-dotenv` in `settings.py`.

---

# 4. Database

## MySQL (Docker recommended)

If you prefer MySQL in Docker, use the following docker run command (adjust envs):

```bash
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=mydb -e MYSQL_USER=myuser -e MYSQL_PASSWORD=mypass \
  -p 3306:3306 -v mysql_data:/var/lib/mysql -d mysql:latest
```

Then set `.env`:

```
DB_ENGINE=django.db.backends.mysql
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypass
DB_HOST=127.0.0.1/'localhost'
DB_PORT=3306
```

> If you mapped host port to something other than 3306 (e.g., 3307), use that port in `DB_PORT`.

---

# 5. Running migrations & creating a superuser

```bash
python manage.py makemigrations
python manage.py migrate

# create admin
python manage.py createsuperuser
```

 Start the dev server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

---

# 6. Project structure (example)

```
project-root/
├─ manage.py
├─ requirements.txt
├─ .env              # not committed but there is sample_env
├─ README.md
├─ appname/
│  ├─ migrations/
│  ├─ templates/
│  ├─ static/
│  ├─ views.py
│  ├─ urls.py
│  └─ ...
├─ project_name/
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
└─ templates/
```


