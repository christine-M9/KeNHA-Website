
import React, { useState } from 'react';

function NewTaskForm() {
  const [formData, setFormData] = useState({
    title: '',
    location: '',
    maintenanceType: '',
    estimatedCompletionTime: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch('/api/tasks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log('New task created:', data);
      
      // Reset the form after successful submission
      setFormData({
        title: '',
        location: '',
        maintenanceType: '',
        estimatedCompletionTime: '',
      });
    } catch (error) {
      console.error('Error creating new task:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Title:
        <input
          type="text"
          name="title"
          value={formData.title}
          onChange={handleChange}
        />
      </label>
      <label>
        Location:
        <input
          type="text"
          name="location"
          value={formData.location}
          onChange={handleChange}
        />
      </label>
      <label>
        Maintenance Type:
        <input
          type="text"
          name="maintenanceType"
          value={formData.maintenanceType}
          onChange={handleChange}
        />
      </label>
      <label>
        Estimated Completion Time:
        <input
          type="text"
          name="estimatedCompletionTime"
          value={formData.estimatedCompletionTime}
          onChange={handleChange}
        />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}

export default NewTaskForm;
