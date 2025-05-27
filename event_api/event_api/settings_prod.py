from .settings import *  # import base settings

import os
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['your-render-app-name.onrender.com']

# Configure database from env variable
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://user:password@localhost:5432/dbname',
        conn_max_age=600,
        ssl_require=True
    )
}

# Static files settings (if using WhiteNoise for static file serving)
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Add WhiteNoise middleware for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    *MIDDLEWARE[1:],  # keep your other middleware
]

# Security settings - tweak as needed
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Secret key from env
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
