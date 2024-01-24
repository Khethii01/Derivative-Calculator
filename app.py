from flask import Flask, render_template, request
from sympy import symbols, diff, simplify, latex

app = Flask(__name__)

@app.route('/') # route to main page(index.html)
def index():
    return render_template('index.html') # render HTML template w/o results

@app.route('/calculate_derivative', methods=['POST']) # route to handle calculations
def calculate_derivative():
    expression = request.form['expression']

    x = symbols('x')

    try:
        expr = eval(expression) # evaluate string as a python expression
        derivative = diff(expr, x)
        simplified_derivative = simplify(derivative)
        result = str(simplified_derivative) # convert result to string for displaying

    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('index.html', expression=expression, result=result) # render HTML template w/ results

# start flask application with debugging enabled
if __name__ == '__main__':
    app.run(debug=True)
