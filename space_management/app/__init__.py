from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    ma.init_app(app)
    
    # Enable CORS
    CORS(app)
    
    from app.routes import main, missions, celestial_bodies
    app.register_blueprint(main.bp)
    app.register_blueprint(missions.bp, url_prefix='/missions')
    app.register_blueprint(celestial_bodies.bp, url_prefix='/celestial_bodies')
    
    return app