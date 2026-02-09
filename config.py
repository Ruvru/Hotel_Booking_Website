import os
from datetime import timedelta

class Config:
    secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    #Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///hotel_booking.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Session configuration
    permanent_session_lifetime = timedelta(minutes=7)
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'LAX'

    #Upload folder images
    upload_folder='static/images/uploads'
    max_content_length= 16*1024*1024