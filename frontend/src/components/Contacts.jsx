import React, { useState, useEffect } from 'react';

function Contacts() {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    fetch('api/contacts')
      .then(response => response.json())
      .then(data => setContacts(data))
      .catch(error => console.error('Error fetching contacts:', error));
  }, []);

  return (
    <div>
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

export default Contacts;
