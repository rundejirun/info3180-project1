"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
from app.forms import PropertyForm
from app.models import Property

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Ayodeji Adedipe")

@app.route('/properties/create', methods= ['GET', 'POST'])
def create():
    """For displaying the form to add a new
property."""

    form = PropertyForm()
    if request.method == 'POST':
    
        if form.validate_on_submit():
            title= form.title.data
            bedrooms= form.bedrooms.data
            bathrooms= form.bathrooms.data
            location = form.location.data
            price = form.price.data
            proptype = form.proptype.data
            description = form.description.data
            
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            
            prop = Property (title=title, description=description, bedrooms=bedrooms, bathrooms=bathrooms, price=price, location=location, proptype=proptype, photo=filename)
            db.session.add(prop)
            db.session.commit()
            
            flash ('Form submitted successfully', 'success')
            return redirect(url_for('properties'))
    flash_errors(form)
    return render_template('create.html', form= form)

@app.route('/properties')
def properties():
    """For displaying a list of all properties in the
database"""
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def property(propertyid):
    """For viewing an individual property
by the specific property id."""
    propertyid = int(propertyid)
    property = Property.query.filter_by(id=propertyid).first()
    return render_template("property.html",property=property)
    
@app.route("/uploads/<filename>")
def getPhoto(filename):
    root = os.getcwd()
    return send_from_directory(os.path.join(root,app.config["UPLOAD_FOLDER"]),filename)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
