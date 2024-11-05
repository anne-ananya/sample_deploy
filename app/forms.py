from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class FacultyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    research_area = StringField('Research Area', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AlumniForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    year_of_graduation = IntegerField('Year of Graduation', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    current_position = StringField('Current Position', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    contact_info = StringField('Contact Info', validators=[DataRequired()])
    submit = SubmitField('Submit')
