from flask import request, jsonify, current_app
from .models import SpaceObject
from . import db

@current_app.route('/objects', methods=['GET'])
def get_objects():
    objects = SpaceObject.query.all()
    return jsonify([obj.to_dict() for obj in objects])

@current_app.route('/objects', methods=['POST'])
def add_object():
    data = request.json
    new_object = SpaceObject(name=data['name'], description=data.get('description'), coordinates=data['coordinates'])
    db.session.add(new_object)
    db.session.commit()
    return jsonify(new_object.to_dict()), 201
