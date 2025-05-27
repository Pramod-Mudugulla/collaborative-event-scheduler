# 🗓️ Event Scheduler API

A Django REST API for creating, sharing, and managing events with collaborative editing. Built with a focus on role-based access control, recurring events, and scalable architecture.

---

## 🚀 Features

- User registration and JWT-based authentication
- Create, view, edit, delete events
- Support for recurring events (`daily`, `weekly`, `monthly`)
- Role-based permissions: `owner`, `editor`, `viewer`
- Event sharing with granular access control
- View and edit access for collaborators based on role
- Swagger documentation via `drf-spectacular`

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework
- **Auth:** JWT (SimpleJWT)
- **Docs:** drf-spectacular (Swagger UI)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/event-scheduler.git
cd event-scheduler

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
