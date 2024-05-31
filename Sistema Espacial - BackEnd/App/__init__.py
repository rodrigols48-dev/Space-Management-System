from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api 
from flask_cors import CORS
from config import Config
app = Flask(__name__)
CORS(app)
api = Api(app)

db = SQLAlchemy()
ma = Marshmallow()

from App.Routes.celestial_bodies import create_celestial_body,update_celestial_body, delete_celestial_body
api.add_resource(Index, '/') #como se fosse a rota, so que com a chamada da api
api.add_resource(create_celestial_body, '/criar')
api.add_resource(update_celestial_body, '/atualizar')
api.add_resource(delete_celestial_body, '/deletar')

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    ma.init_app(app)
    
    # Enable CORS
    CORS(app)
    
    from App.Routes import main, missions, celestial_bodies
    app.register_blueprint(main.bp)
    app.register_blueprint(missions.bp, url_prefix='/missions')
    app.register_blueprint(celestial_bodies.bp, url_prefix='/celestial_bodies')
    
    return app