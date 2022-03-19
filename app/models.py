from . import db

class Property(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    bedrooms = db.Column(db.String(10))
    bathrooms = db.Column(db.String(10))
    price = db.Column(db.String(30))
    proptype = db.Column(db.String(20))
    location = db.Column(db.String(200), unique=True)
    photo = db.Column(db.String(150))

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
