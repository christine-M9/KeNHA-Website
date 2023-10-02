from backend import app, db
from backend.models import Project, Service, User
from flask import request, jsonify

# Define routes here
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.serialize() for project in projects])

# Add other routes (create, update, delete) as needed
