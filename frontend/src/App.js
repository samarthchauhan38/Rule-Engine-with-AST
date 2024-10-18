import React, { useState } from 'react';
import RuleInput from './components/RuleInput';
import ASTVisualizer from './components/ASTVisualizer';
import RuleEvaluator from './components/RuleEvaluator';

function App() {
  const [astData, setAstData] = useState(null);
  const [evaluationResult, setEvaluationResult] = useState(null);

  const parseRule = async (rule) => {
    try {
      const response = await fetch('http://localhost:5000/parse-rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule }),
      });
      const data = await response.json();
      if (response.ok) {
        setAstData(data); // Set parsed AST
      } else {
        console.error('Error:', data.error);
      }
    } catch (error) {
      console.error('Error parsing rule:', error);
    }
  };

  const evaluateRule = async (userData) => {
    try {
      const response = await fetch('http://localhost:5000/evaluate-rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ast: astData, userData }),
      });
      const data = await response.json();
      if (response.ok) {
        setEvaluationResult(data.result);
      } else {
        console.error('Error:', data.error);
      }
    } catch (error) {
      console.error('Error evaluating rule:', error);
    }
  };

  return (
    <div className="App">
      <h1>Rule Engine Frontend</h1>
      
      {/* Rule Input */}
      <RuleInput onSubmit={parseRule} />

      {/* AST Visualization */}
      <h2>AST Visualization</h2>
      <ASTVisualizer astData={astData} />

      {/* Rule Evaluation */}
      <h2>Evaluate Rule</h2>
      <RuleEvaluator onSubmit={evaluateRule} />
      
      {/* Display Evaluation Result */}
      {evaluationResult !== null && (
        <div>
          <h3>Evaluation Result:</h3>
          <p>{evaluationResult ? "True" : "False"}</p>
        </div>
      )}
    </div>
  );
}

export default App;
