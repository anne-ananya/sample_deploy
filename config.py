import os
class Config:
    SECRET_KEY  = os.getenv('SECRET_KEY', os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.getenv('Database_URL', 'postgresql+pg8000://default:VzfUK9iA3IJO@ep-red-pine-a4xps3a8-pooler.us-east-1.aws.neon.tech:5432/verceldb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# Ensure the folder exists
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)