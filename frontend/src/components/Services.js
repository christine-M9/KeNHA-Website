
import React, { useState, useEffect } from 'react';

function Services() {
  const [services, setServices] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/services')
      .then(response => response.json())
      .then(data => setServices(data));
  }, []);

  return (
    <div>
      <h1>Services</h1>
      <ul>
        {services.map(service => (
          <li key={service.id}>
            <strong>{service.title}</strong>: {service.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Services;
