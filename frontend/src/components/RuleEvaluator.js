import React, { useState } from 'react';

const RuleEvaluator = ({ onSubmit }) => {
  const [userData, setUserData] = useState({
    age: '',
    department: '',
    salary: '',
    experience: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(userData);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <h3>Enter User Data:</h3>
        <label>Age:</label>
        <input
          type="number"
          value={userData.age}
          onChange={(e) => setUserData({ ...userData, age: e.target.value })}
        />
        <label>Department:</label>
        <input
          type="text"
          value={userData.department}
          onChange={(e) => setUserData({ ...userData, department: e.target.value })}
        />
        <label>Salary:</label>
        <input
          type="number"
          value={userData.salary}
          onChange={(e) => setUserData({ ...userData, salary: e.target.value })}
        />
        <label>Experience:</label>
        <input
          type="number"
          value={userData.experience}
          onChange={(e) => setUserData({ ...userData, experience: e.target.value })}
        />
        <button type="submit">Evaluate Rule</button>
      </form>
    </div>
  );
};

export default RuleEvaluator;
