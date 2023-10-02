from faker import Faker
from app import app, db, Project, Service, Contact

fake = Faker()

# Set up app context
with app.app_context():

    # Seed projects
    for _ in range(5):
        project = Project(
            title=fake.sentence(),
            description=fake.paragraph()
        )
        db.session.add(project)

        # Seed services and associating them with the project
        for _ in range(fake.random_int(min=1, max=5)):  
            service = Service(
                title=fake.sentence(),
                description=fake.paragraph()
            )
            project.services.append(service)

    # Seed contacts
    for _ in range(5):
        contact = Contact(
            name=fake.name(),
            email=fake.email(),
            message=fake.paragraph(),
            project_id=fake.random_int(min=1, max=5)  
        )
        db.session.add(contact)

    # Commit the changes
    db.session.commit()


