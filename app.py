from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='frontend/dist', static_url_path='/')

@app.route('/api/planets')
def get_planets():
    # Aqui você pode fornecer dados sobre planetas
    planets = [
        {"name": "Mercury", "description": "Closest to the Sun"},
        {"name": "Venus", "description": "Second planet from the Sun"},
        {"name": "Earth", "description": "Our home planet"},
        {"name": "Mars", "description": "Red planet"}
    ]
    return jsonify(planets)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
