# app.py
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
logging.basicConfig(level=logging.DEBUG)
import traceback

# AST Node Definition
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left  # Left child (for operators)
        self.right = right  # Right child (for operators)
        self.value = value  # Condition or operator

    def __repr__(self):
        if self.node_type == "operand":
            return f"Operand({self.value})"
        return f"Operator({self.value})"


# Error Handling
class RuleEngineError(Exception):
    pass

class InvalidRuleStringError(RuleEngineError):
    def __init__(self, message="Invalid rule string format"):
        self.message = message
        super().__init__(self.message)

class UnsupportedComparisonError(RuleEngineError):
    def __init__(self, message="Unsupported comparison in rule"):
        self.message = message
        super().__init__(self.message)


# Valid Fields and Validation Functions
VALID_FIELDS = ['age', 'department', 'salary', 'experience']

def validate_rule_string(rule_string):
    if rule_string.count('(') != rule_string.count(')'):
        raise InvalidRuleStringError("Unbalanced parentheses in rule string.")
    if not any(op in rule_string for op in ["==", ">", "<"]):
        raise InvalidRuleStringError("Missing or invalid operators in rule string.")

def validate_attributes(rule_string):
    operators = ['AND', 'OR', '>', '<', '==', '(', ')']
    tokens = rule_string.replace('(', '').replace(')', '').split(' ')
    attributes = [token for token in tokens if token.isalpha() and token not in operators]
    
    for attr in attributes:
        if attr not in VALID_FIELDS:
            raise InvalidRuleStringError(f"Invalid attribute: {attr}")


# Creating the Rule (AST Construction)
def create_rule(rule_string):
    validate_rule_string(rule_string)  # Validate the rule format
    validate_attributes(rule_string)   # Ensure only valid attributes are used

    # Tokenize the rule string
    tokens = re.split(r"(\s+|\(|\)|AND|OR)", rule_string)
    tokens = [token.strip() for token in tokens if token.strip()]

    def parse_expression(tokens):
        if not tokens:
            raise InvalidRuleStringError("No tokens found, invalid rule string.")

        # Parse for parentheses
        if tokens[0] == '(':
            sub_tokens = []
            balance = 0
            for token in tokens:
                if token == '(':
                    balance += 1
                elif token == ')':
                    balance -= 1
                sub_tokens.append(token)
                if balance == 0:
                    return parse_expression(sub_tokens[1:-1])  # Recursively parse sub-expression
            
            if balance != 0:
                raise InvalidRuleStringError("Unbalanced parentheses in rule string.")
        
        # Parse for AND/OR operators
        for i, token in enumerate(tokens):
            if token in ['AND', 'OR']:
                left = parse_expression(tokens[:i])
                right = parse_expression(tokens[i+1:])
                return Node("operator", left=left, right=right, value=token)

        # Remaining tokens should be an operand
        if len(tokens) == 3:  # Operand should have 3 parts: attribute, operator, value
            return Node("operand", value=" ".join(tokens))
        
        raise InvalidRuleStringError("Invalid operand format in rule string.")
    
    # Build the AST
    try:
        ast = parse_expression(tokens)
        return ast
    except Exception as e:
        raise InvalidRuleStringError(f"Error while creating AST: {str(e)}")


# Combining Rules
def combine_rules(rules):
    if not rules:
        raise ValueError("No rules provided for combination.")
    
    asts = [create_rule(rule) for rule in rules]
    combined_root = asts[0]
    
    for ast in asts[1:]:
        combined_root = Node("operator", left=combined_root, right=ast, value="OR")

    return combined_root


# Evaluating the Rule
def eval_condition(condition, data):
    key, operator, value = condition.split()  # Example: "age > 30"
    
    # Get the value from data
    data_value = data.get(key)

    # Handle potential type conversion
    try:
        value = int(value)
    except ValueError:
        value = value.strip("'")

    if isinstance(data_value, (int, float)) and isinstance(value, (int, float)):
        if operator == ">":
            return data_value > value
        elif operator == "<":
            return data_value < value
        elif operator == "==":
            return data_value == value
        elif operator == ">=":
            return data_value >= value
        elif operator == "<=":
            return data_value <= value

    elif isinstance(data_value, str) and isinstance(value, str):
        if operator == "==":
            return data_value == value
    
    raise UnsupportedComparisonError(f"Unsupported operator: {operator}")


def evaluate_rule(ast, data):
    if ast is None:
        raise ValueError("AST is None; cannot evaluate rule.")
    
    # Debugging: Print the current node being evaluated
    print(f"Evaluating node: {ast}")

    if ast.node_type == "operand":
        # Evaluate the condition based on the operand node
        return eval_condition(ast.value, data)
    
    elif ast.node_type == "operator":
        if ast.value == "AND":
            left_result = evaluate_rule(ast.left, data)
            right_result = evaluate_rule(ast.right, data)
            return left_result and right_result
        
        elif ast.value == "OR":
            left_result = evaluate_rule(ast.left, data)
            right_result = evaluate_rule(ast.right, data)
            return left_result or right_result
    
    # Raise an error for unsupported node types
    raise ValueError(f"Unsupported node type: {ast.node_type}")


# Flask App
app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/parse-rule', methods=['POST'])
def parse_rule():
    data = request.get_json()
    rule_string = data.get('rule')
    try:
        ast = create_rule(rule_string)
        # Convert AST object into a serializable format
        def serialize_ast(node):
            if node is None:
                return None
            return {
                "node_type": node.node_type,
                "value": node.value,
                "left": serialize_ast(node.left),
                "right": serialize_ast(node.right)
            }
        serialized_ast = serialize_ast(ast)
        return jsonify(serialized_ast), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    
#@app.route('/evaluate-rule', methods=['POST'])    
def dict_to_node(ast_dict):
    if ast_dict['node_type'] == 'operand':
        return Node(node_type='operand', value=ast_dict['value'])
    elif ast_dict['node_type'] == 'operator':
        left_node = dict_to_node(ast_dict['left']) if 'left' in ast_dict else None
        right_node = dict_to_node(ast_dict['right']) if 'right' in ast_dict else None
        return Node(node_type='operator', left=left_node, right=right_node, value=ast_dict['value'])
    else:
        raise ValueError("Invalid node type in AST")
    

@app.route('/evaluate-rule', methods=['POST'])
def evaluate_rule_api():
    # Initialize variables
    ast = None
    user_data = None

    # Attempt to get JSON data from the request
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        ast_dict = data.get('ast')  # Get the AST as a dictionary
        user_data = data.get('userData')

        # Debugging: Print the received data
        print(f"Received AST: {ast_dict}")
        print(f"Received user data: {user_data}")

        if ast_dict is None or user_data is None:
            return jsonify({"error": "Invalid input data"}), 400

        # Convert user data types
        user_data['age'] = int(user_data['age'])
        user_data['salary'] = int(user_data['salary'])
        user_data['experience'] = int(user_data['experience'])
        
        # Convert AST dictionary to Node
        ast = dict_to_node(ast_dict)

        # Proceed to evaluate the rule using your existing function
        result = evaluate_rule(ast, user_data)  # Now 'ast' is a Node object
        return jsonify({"result": result}), 200
    
    except Exception as e:
        print("Error occurred:", str(e))
        print(traceback.format_exc())  # This will print the full traceback to the console
        return jsonify({"error": str(e)}), 500




if __name__ == '__main__':
    app.run(debug=True)
