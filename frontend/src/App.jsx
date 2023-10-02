import React, { useState, useEffect } from 'react';

function App() {
  const [projects, setProjects] = useState([]);
  const [services, setServices] = useState([]);
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    // Fetch projects
    fetch('api/projects')
      .then(response => response.json())
      .then(data => setProjects(data))
      .catch(error => console.error('Error fetching projects:', error));


    // Fetch services
    fetch('api/services')
      .then(response => response.json())
      .then(data => setServices(data))
      .catch(error => console.error('Error fetching services:', error));

    // Fetch contacts
    fetch('api/contacts')
      .then(response => response.json())
      .then(data => setContacts(data))
      .catch(error => console.error('Error fetching contacts:', error));
  }, []);

  return (
    <div>
      <h1>WELCOME TO KENYA NATIONAL HIGHWAYS AUTHORITY</h1>

      <h2>Projects</h2>
      <ul>
        {projects.map(project => (
          <li key={project.id}>
            Title: {project.title}, Description: {project.description}
          </li>
        ))}
      </ul>

      <h2>Services</h2>
      <ul>
        {services.map(service => (
          <li key={service.id}>
            Title: {service.title}, Description: {service.description}
          </li>
        ))}
      </ul>

      <h2>Contacts</h2>
      <ul>
        {contacts.map(contact => (
          <li key={contact.id}>
            Name: {contact.name}, Email: {contact.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
