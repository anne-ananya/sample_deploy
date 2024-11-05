from app import db


class Faculty(db.Model):
    __tablename__ = 'faculty'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20))
    research_area = db.Column(db.String(100))
    image_url = db.Column(db.String(255))  # Ensure this line exists

class Alumni(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year_of_graduation = db.Column(db.Integer)
    department = db.Column(db.String(100))
    current_position = db.Column(db.String(100))
    email = db.Column(db.String(100))
    contact_info = db.Column(db.Text)
