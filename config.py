import os

class Config:
    SECRET_KEY  = '1a52ece65ce46d41b23917a2a98c88bf'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost/iiestportal'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the folder exists
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)