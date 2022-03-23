from . import db

class Property(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.Text())
    bedrooms = db.Column(db.String())
    bathrooms = db.Column(db.String(500))
    price = db.Column(db.String())
    proptype = db.Column(db.String())
    location = db.Column(db.String())
    photo = db.Column(db.String())

    def __init__(self, title, description, bedrooms, bathrooms, price, proptype, location, photo):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.proptype = proptype
        self.location = location
        self.photo = photo
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % self.title
