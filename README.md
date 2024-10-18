Rule Engine with Abstract Syntax Tree (AST)
Project Overview
This project implements a Rule Engine that allows users to define rules based on conditions like age, department, salary, and experience. These rules are parsed into an Abstract Syntax Tree (AST), visualized for the user, and then evaluated against input data. The frontend is built using React, while the backend is built with Flask and Python. The communication between the frontend and backend is handled via RESTful API calls.

Key Features
User-defined Rules: Users can input rules such as (age > 30 AND department == 'Sales').
Abstract Syntax Tree (AST): The rules are parsed into an AST structure and visualized for better understanding.
Rule Evaluation: The user-defined rules are evaluated against real-time user input (age, department, salary, experience).
React Frontend: A dynamic and interactive UI allows the user to input rules and data and view the results in real-time.
Flask Backend: Handles rule parsing, AST generation, and rule evaluation logic.

Dependencies
Backend Dependencies
The backend requires Python 3.x and the following dependencies (listed in requirements.txt):

Flask: A lightweight WSGI web application framework.
Flask-CORS: To handle cross-origin requests between the frontend and backend.
AST parsing libraries: To build and evaluate AST from user-defined rules.
JSON: For parsing data sent between frontend and backend.
Frontend Dependencies
The frontend is built with React. Dependencies include:

React: JavaScript library for building the user interface.
react-d3-tree: For visualizing the AST structure of the rules.
axios: For making HTTP requests to the backend.


Installation and Setup

Backend Setup
Navigate to the backend directory:
cd backend
python app.py

Frontend Setup
Navigate to the frontend directory:
npm install
npm start
