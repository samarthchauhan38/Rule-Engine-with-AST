import React, { useState } from 'react';

const RuleInput = ({ onSubmit }) => {
  const [rule, setRule] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(rule);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>Enter Rule:</label>
        <input
          type="text"
          value={rule}
          onChange={(e) => setRule(e.target.value)}
          placeholder="(age > 30 AND department == 'Sales')"
        />
        <button type="submit">Parse Rule</button>
      </form>
    </div>
  );
};

export default RuleInput;
