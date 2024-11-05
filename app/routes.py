import os
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from app.models import db, Faculty, Alumni

# Create a Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

# Display Faculty Information
@main.route('/faculty')
def faculty():
    faculty_list = Faculty.query.all()  # Query all faculty records
    return render_template('faculty.html', faculty_list=faculty_list)

# Add Faculty
@main.route('/add_faculty', methods=['POST'])
def add_faculty():
    name = request.form['name']
    department = request.form['department']
    email = request.form['email']
    phone = request.form['phone']
    research_area = request.form['research_area']
    image_file = request.files['image']
    
    # Process the image
    if image_file and image_file.filename != '':
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        image_file.save(image_path)
        image_url = f'uploads/{filename}'  # Save relative path
    else:
        image_url = None  # Handle cases without an image

    # Save to the database
    new_faculty = Faculty(name=name, department=department, email=email,
                          phone=phone, research_area=research_area, image_url=image_url)
    db.session.add(new_faculty)
    db.session.commit()
    
    return redirect(url_for('main.faculty'))

# Update Faculty
@main.route('/faculty/update/<int:faculty_id>', methods=['POST'])
def update_faculty(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    
    # Get form data
    name = request.form.get('name')
    department = request.form.get('department')
    email = request.form.get('email')
    phone = request.form.get('phone')
    research_area = request.form.get('research_area')

    # Validate fields
    if not name or not department or not email:
        flash("Name, Department, and Email are required fields.")
        return redirect(url_for('main.faculty'))

    # Update faculty details
    faculty.name = name
    faculty.department = department
    faculty.email = email
    faculty.phone = phone
    faculty.research_area = research_area
    
    db.session.commit()
    flash("Faculty updated successfully!")
    return redirect(url_for('main.faculty'))

# Delete Faculty
@main.route('/faculty/delete/<int:faculty_id>', methods=['POST'])
def delete_faculty(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    db.session.delete(faculty)
    db.session.commit()
    flash("Faculty deleted successfully!")
    return redirect(url_for('main.faculty'))


# Display Alumni Information
@main.route('/alumni')
def alumni():
    alumni_list = Alumni.query.all()
    return render_template('alumni.html', alumni=alumni_list)

# Add a new alumni
@main.route('/add_alumni', methods=['GET', 'POST'])
def add_alumni():
    if request.method == 'POST':
        name = request.form['name']
        year_of_graduation = request.form['year_of_graduation']
        department = request.form['department']
        current_position = request.form.get('current_position')
        email = request.form.get('email')
        contact_info = request.form.get('contact_info')
        
        new_alumni = Alumni(
            name=name,
            year_of_graduation=year_of_graduation,
            department=department,
            current_position=current_position,
            email=email,
            contact_info=contact_info
        )
        
        try:
            db.session.add(new_alumni)
            db.session.commit()
            flash("Alumni added successfully!", "success")
            return redirect(url_for('main.alumni'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding alumni: {str(e)}", "danger")
    return render_template('main.add_alumni.html')

# Update an existing alumni
@main.route('/update_alumni/<int:id>', methods=['GET', 'POST'])
def update_alumni(id):
    alumni = Alumni.query.get_or_404(id)
    if request.method == 'POST':
        alumni.name = request.form['name']
        alumni.year_of_graduation = request.form['year_of_graduation']
        alumni.department = request.form['department']
        alumni.current_position = request.form.get('current_position')
        alumni.email = request.form.get('email')
        alumni.contact_info = request.form.get('contact_info')
        
        try:
            db.session.commit()
            flash("Alumni updated successfully!", "success")
            return redirect(url_for('main.alumni'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating alumni: {str(e)}", "danger")
    return render_template('main.update_alumni.html', alumni=alumni)

# Delete an alumni
@main.route('/delete_alumni/<int:id>', methods=['POST'])
def delete_alumni(id):
    alumni = Alumni.query.get_or_404(id)
    try:
        db.session.delete(alumni)
        db.session.commit()
        flash("Alumni deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting alumni: {str(e)}", "danger")
    return redirect(url_for('main.alumni'))