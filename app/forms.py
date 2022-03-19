from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import *

class PropertyForm(FlaskForm):
    title= StringField('Title', validators=[DataRequired()])
    bedrooms= StringField('Number of Bedrooms', validators=[DataRequired()])
    bathrooms= StringField('Number of Bathrooms', validators=[DataRequired()])
    location= StringField('Location', validators=[DataRequired()])
    price= StringField('Price', validators=[DataRequired()])
    proptype = SelectField('Property Type', validators=None, choices=[('House', "House"), ('Apartment','Apartment')])
    description= TextAreaField('Description', validators=[DataRequired()])
    
    photo = FileField('Photo', validators = [FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])