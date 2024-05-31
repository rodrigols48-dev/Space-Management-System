from App import db

class Mission(db.Model):
    id = db.Column(db.Integer, ForeignKey = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = False)
    launch_date = db.Column(db.Date, nullable = False)
    status = db.Column(db.String(50), nullable = False)

class Celestial_Bodies(db.Model):
    id = db.Column(db.Integer, ForeignKey = True)
    name = db.Column(db.String(100), nullable = False)
    type = db.Column(db.String(50), nullable = False)

            # Planet, Moons, Star, etc:

    description = db.Column(db.Text, nullable = False)
    discovery_date = db.Column(db.Date, nullable = True)
    discovery_by = db.Column(db.String(100), nullable = True)