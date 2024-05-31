from App import ma
from App.models import Mission
from marshmallow import fields

class MissionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mission
        load_instance = True

    launch_date = fields.Date(format='%Y-%M-%D')

mission_schema = MissionSchema()
missions_schema = MissionSchema(many=True)