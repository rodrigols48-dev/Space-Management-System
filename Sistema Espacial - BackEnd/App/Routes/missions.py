from flask import Blueprint, request, jsonify
from App.models import Mission
from App.Schemas.missions_schema import mission_schema, missions_schema
from App import db

bp = Blueprint('missions', __name__)

@bp.route('/', methods=['GET'])
def get_missions():
    try:
        missions = Mission.query.all()
        return missions_schema.jsonify(missions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/<int:id>', methods=['GET'])
def get_mission(id):
    try:
        mission = Mission.query.get_or_404(id)
        return mission_schema.jsonify(mission), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/', methods=['POST'])
def create_mission():
    try:
        data = request.get_json()
        errors = mission_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        mission = mission_schema.load(data)
        db.session.add(mission)
        db.session.commit()
        return mission_schema.jsonify(mission), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@bp.route('/<int:id>', methods=['PUT'])
def update_mission(id):
    try:
        mission = Mission.query.get_or_404(id)
        data = request.get_json()
        errors = mission_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        mission.name = data.get('name', mission.name)
        mission.description = data.get('description', mission.description)
        mission.launch_date = data.get('launch_date', mission.launch_date)
        mission.status = data.get('status', mission.status)
        db.session.commit()
        return mission_schema.jsonify(mission), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@bp.route('/<int:id>', methods=['DELETE'])
def delete_mission(id):
    try:
        mission = Mission.query.get_or_404(id)
        db.session.delete(mission)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500