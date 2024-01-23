# Import necessary modules from Flask and sympy libraries
from flask import Flask, render_template, request
from sympy import symbols, diff, simplify, latex

# Create a Flask web application
app = Flask(__name__)

# Define a route for the main page (index)
@app.route('/')
def index():
    # Render the HTML template for the main page
    return render_template('index.html')

# Define a route for handling the derivative calculation
@app.route('/calculate_derivative', methods=['POST'])
def calculate_derivative():
    # Get the mathematical expression from the form submitted by the user
    expression = request.form['expression']

    # Define the variable 'x' for symbolic mathematics
    x = symbols('x')

    try:
        # Evaluate the expression entered by the user
        expr = eval(expression)

        # Calculate the derivative of the expression
        derivative = diff(expr, x)

        # Simplify the result of the derivative calculation
        simplified_derivative = simplify(derivative)

        # Convert the result to a string for displaying
        result = str(simplified_derivative)

    except Exception as e:
        # Handle errors in case of invalid input or other exceptions
        result = f"Error: {str(e)}"

    # Render the HTML template with the expression and result to display
    return render_template('index.html', expression=expression, result=result)

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
