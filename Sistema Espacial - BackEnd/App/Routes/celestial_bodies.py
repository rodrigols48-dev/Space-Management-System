from flask import Blueprint, request, jsonify
from app.models import CelestialBody
from app.schemas.celestial_body_schema import celestial_body_schema, celestial_bodies_schema
from app import db

bp = Blueprint('celestial_bodies', __name__)

@bp.route('/', methods=['GET'])
def get_celestial_bodies():
    try:
        bodies = CelestialBody.query.all()
        return celestial_bodies_schema.jsonify(bodies), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/<int:id>', methods=['GET'])
def get_celestial_body(id):
    try:
        body = CelestialBody.query.get_or_404(id)
        return celestial_body_schema.jsonify(body), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/', methods=['POST'])
def create_celestial_body():
    try:
        data = request.get_json()
        errors = celestial_body_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        body = celestial_body_schema.load(data)
        db.session.add(body)
        db.session.commit()
        return celestial_body_schema.jsonify(body), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@bp.route('/<int:id>', methods=['PUT'])
def update_celestial_body(id):
    try:
        body = CelestialBody.query.get_or_404(id)
        data = request.get_json()
        errors = celestial_body_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        body.name = data.get('name', body.name)
        body.type = data.get('type', body.type)
        body.description = data.get('description', body.description)
        body.discovery_date = data.get('discovery_date', body.discovery_date)
        body.discovered_by = data.get('discovered_by', body.discovered_by)
        db.session.commit()
        return celestial_body_schema.jsonify(body), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@bp.route('/<int:id>', methods=['DELETE'])
def delete_celestial_body(id):
    try:
        body = CelestialBody.query.get_or_404(id)
        db.session.delete(body)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500