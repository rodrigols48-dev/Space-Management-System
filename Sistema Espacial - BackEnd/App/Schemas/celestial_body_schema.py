from App import ma
from App.models import CelestialBody
from marshmallow import fields

class CelestialBodySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CelestialBody
        load_instance = True

    discovery_date = fields.Date(format='%Y-%M-%D', allow_none=True)

celestial_body_schema = CelestialBodySchema()
celestial_bodies_schema = CelestialBodySchema(many=True)