from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Project, Service, Contact

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kenha_website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


with app.app_context():
    db.create_all()


# Routes for projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.serialize() for project in projects])

@app.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    project = Project(title=title, description=description)
    db.session.add(project)
    db.session.commit()
    return jsonify(project.serialize()), 201

@app.route('/projects/<int:id>', methods=['PUT'])
def update_project(id):
    project = Project.query.get(id)
    if not project:
        return jsonify({'message': 'Project not found'}), 404

    data = request.get_json()
    project.title = data.get('title', project.title)
    project.description = data.get('description', project.description)
    db.session.commit()
    return jsonify(project.serialize())

@app.route('/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    project = Project.query.get(id)
    if project:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted'})
    else:
        return jsonify({'message': 'Project not found'}), 404

# Routes for services
@app.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([service.serialize() for service in services])

@app.route('/services', methods=['POST'])
def create_service():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    service = Service(title=title, description=description)
    db.session.add(service)
    db.session.commit()
    return jsonify(service.serialize()), 201

@app.route('/services/<int:id>', methods=['PUT'])
def update_service(id):
    service = Service.query.get(id)
    if not service:
        return jsonify({'message': 'Service not found'}), 404

    data = request.get_json()
    service.title = data.get('title', service.title)
    service.description = data.get('description', service.description)
    db.session.commit()
    return jsonify(service.serialize())

@app.route('/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    service = Service.query.get(id)
    if service:
        db.session.delete(service)
        db.session.commit()
        return jsonify({'message': 'Service deleted'})
    else:
        return jsonify({'message': 'Service not found'}), 404

# Routes for contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([contact.serialize() for contact in contacts])

@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    contact = Contact(name=name, email=email)
    db.session.add(contact)
    db.session.commit()
    return jsonify(contact.serialize()), 201

@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({'message': 'Contact not found'}), 404

    data = request.get_json()
    contact.name = data.get('name', contact.name)
    contact.email = data.get('email', contact.email)
    db.session.commit()
    return jsonify(contact.serialize())

@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    if contact:
        db.session.delete(contact)
        db.session.commit()
        return jsonify({'message': 'Contact deleted'})
    else:
        return jsonify({'message': 'Contact not found'}), 404


@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    location = data.get('location')
    maintenance_type = data.get('maintenanceType')
    estimated_completion_time = data.get('estimatedCompletionTime')
    task = Task(
        title=title,
        location=location,
        maintenance_type=maintenance_type,
        estimated_completion_time=estimated_completion_time
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.serialize()), 201


if __name__ == '__main__':
    app.run(debug=True)

