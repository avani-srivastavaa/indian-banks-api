import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL',
    'postgresql://postgres:pgadmin@localhost:5432/indian_banks'  # fallback for local dev
).replace('postgres://', 'postgresql://')  # Heroku patch

SQLALCHEMY_TRACK_MODIFICATIONS = False
