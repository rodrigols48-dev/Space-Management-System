from . import db

class SpaceObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    coordinates = db.Column(db.String(100), nullable=False)
