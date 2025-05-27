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

```

## 🔐 Authentication

This project uses JWT authentication.

- **Register:** `POST /api/auth/register/`
- **Login:** `POST /api/auth/login/`
- Use the returned access token in the `Authorization: Bearer <token>` header.

---

## 📘 API Documentation

Interactive Swagger UI available at:


```bash
http://localhost:8000/api/docs/
```


---

## 📬 Key Endpoints

| Method | Endpoint                    | Description                          |
|--------|-----------------------------|--------------------------------------|
| POST   | `/api/auth/register/`       | Register a new user                  |
| POST   | `/api/auth/login/`          | Obtain JWT access & refresh token    |
| POST   | `/api/auth/logout/`         | Blacklist refresh token              |
| GET    | `/api/events/`              | List events (owned or shared)        |
| POST   | `/api/events/`              | Create a single event                |
| POST   | `/api/events/batch/`        | Create multiple events at once       |
| PATCH  | `/api/events/<id>/`         | Update event (owner/editor only)     |
| DELETE | `/api/events/<id>/`         | Delete event (owner only)            |
| POST   | `/api/events/<id>/share/`   | Share event with other users         |

---

## 🧪 Testing

Use Postman or Swagger UI to test all endpoints.

**Sample test cases:**
- ✅ Create event as owner
- ✅ Share event with another user (editor/viewer)
- ✅ Edit event as editor
- ✅ View event as viewer
- ❌ Unauthorized edit/delete as viewer should fail

---

## 📁 Repository Structure

scheduler/
├── models.py # User, Event, EventPermission
├── views.py # ViewSets and business logic
├── serializers.py # Input/output validation
├── permissions.py # Custom role-based permissions
├── urls.py # API routing
├── tests.py # (Optional) Unit tests
└── ...


---

## ✅ Requirements Met

- ✔️ Role-based access
- ✔️ Recurring events
- ✔️ Event sharing with permissions
- ✔️ JWT authentication
- ✔️ Swagger API docs
- ✔️ Error handling with clear messages
- ✔️ Change tracking (`updated_at`)
- ✔️ Clean and modular architecture

---

## 📄 License

MIT License — use freely with attribution.

---

## 🙌 Author

Made by [Pramod Kumar Reddy, Mudugulla] — [pramodmudugulla@gmail.com]
