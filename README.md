# Rule Engine with Abstract Syntax Tree (AST)

## Project Overview

This project implements a **Rule Engine** that allows users to define logical rules based on conditions such as age, department, salary, and experience. The rules are parsed into an **Abstract Syntax Tree (AST)**, visualized for the user, and then evaluated against real-time user input data. 

The project is split into two main parts:
- **Frontend**: Built with React, providing a user interface for rule input, AST visualization, and result display.
- **Backend**: Built using Flask in Python, responsible for parsing the rules, generating the AST, and evaluating it based on the user's input.

---

## Features

- **Dynamic Rule Input**: Users can input custom rules such as `(age > 30 AND department == 'Sales')`.
- **AST Parsing & Visualization**: The rule is parsed into an AST and visualized on the frontend.
- **Rule Evaluation**: The parsed rule is evaluated against user-provided data (age, department, salary, experience).
- **RESTful API**: Communication between the frontend and backend is handled via REST API endpoints.
- **Error Handling**: Provides appropriate error messages for invalid input, missing data, or unsupported operations.

---

## Dependencies

### Backend Dependencies

Make sure you have **Python 3.x** installed and the following Python libraries:

- **Flask**: A lightweight WSGI web application framework.
- **Flask-CORS**: To handle cross-origin requests between the frontend and backend.
- **JSON**: For handling data in JSON format.
- **AST Libraries**: To parse and evaluate the rule logic.

You can install these dependencies by running:

```bash
pip install -r requirements.txt
```

### Frontend Dependencies

The frontend requires **Node.js** and **npm** (Node Package Manager). Install the following npm packages:

- **React**: A JavaScript library for building user interfaces.
- **react-d3-tree**: A library for visualizing hierarchical trees like ASTs.
- **axios**: For making HTTP requests from the frontend to the backend.

Install all frontend dependencies by running:

```bash
npm install
```

---

## Project Structure

```
RuleEngineWithAST/
│
├── backend/                      # Backend (Flask) application
│   ├── app.py                    # Main Flask app with API endpoints
│   ├── rules_engine.py           # Core logic for rule evaluation and AST generation
│   ├── requirements.txt          # Backend dependencies
│
└── frontend/                     # Frontend (React) application
    ├── src/                      # React source files
    │   ├── components/           # React components (ASTVisualizer, RuleForm)
    │   ├── App.js                # Main React app entry point
    │   └── index.js              # React starting point
    ├── public/                   # Public files (HTML, assets)
    ├── package.json              # Frontend dependencies
    └── package-lock.json         # Lock file for npm dependencies
```

---

## Installation and Build Instructions

### Backend Setup

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask server**:
   ```bash
   python app.py
   ```
   This will start the backend on `http://127.0.0.1:5000`. You can now interact with the API endpoints from the frontend.

### Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install frontend dependencies**:
   ```bash
   npm install
   ```

3. **Start the React development server**:
   ```bash
   npm start
   ```
   This will start the frontend on `http://localhost:3000`. The app will automatically reload if you make any changes to the frontend code.

---

## Design Choices

### AST-based Rule Evaluation

The project uses **Abstract Syntax Tree (AST)** for parsing and evaluating rules. When a user submits a rule, it is converted into a tree structure where each node represents an operator (`AND`, `OR`, etc.) or condition (`age > 30`). This design choice makes the rule engine flexible, scalable, and easy to extend with new operators or conditions.

### Separation of Frontend and Backend

The project follows a **separation of concerns** principle:
- The **frontend** handles the user interface, data input, and visualization of the AST.
- The **backend** handles rule parsing, AST generation, and rule evaluation based on input data.

This approach allows for independent development, testing, and deployment of the frontend and backend.

### RESTful API Communication

The communication between the frontend and backend is handled through **RESTful API**. This ensures a clear separation of logic and responsibilities, with the frontend making API requests to evaluate the rules and retrieve results from the backend.

---

## API Endpoints

### 1. **`POST /parse-rule`**
   - Parses a user-defined rule into an AST.
   - **Request Body**:
     ```json
     {
       "rule": "(age > 30 AND department == 'Sales')"
     }
     ```
   - **Response**:
     ```json
     {
       "ast": { /* AST structure */ }
     }
     ```

### 2. **`POST /evaluate-rule`**
   - Evaluates the AST against user data.
   - **Request Body**:
     ```json
     {
       "ast": { /* AST structure */ },
       "userData": {
         "age": 35,
         "department": "Sales",
         "salary": 60000,
         "experience": 5
       }
     }
     ```
   - **Response**:
     ```json
     {
       "result": true
     }
     ```

---

## Example Usage

1. **Input a rule**:
   ``` 
   (age > 30 AND department == 'Sales')
   ```

2. **Enter user data**:
   - Age: `35`
   - Department: `Sales`
   - Salary: `60000`
   - Experience: `5`

3. **Expected result**:
   The rule evaluates to `True` since both conditions (`age > 30` and `department == 'Sales'`) are met.

---

## Future Improvements

- **Operator Expansion**: Currently, only `AND` and `OR` operators are supported. Future versions could include support for `NOT`, comparison operators like `>=`, `<=`, and custom operators.
- **Validation**: More advanced validation is needed to handle invalid rules (e.g., incorrect syntax) before they are parsed.
- **Enhanced Error Handling**: Improve error messages and handling mechanisms to provide users with better feedback during rule creation or evaluation.

---

## Conclusion

This rule engine offers a simple, flexible, and extendable solution for evaluating business logic using rules. By leveraging an AST, the engine can handle complex logical expressions and is designed for scalability. Both the backend and frontend are modular and can be improved independently.

---
![Screenshot 2024-10-18 220119](https://github.com/user-attachments/assets/b07d368e-2eb8-4322-be77-7cbf0ea76cc3)
