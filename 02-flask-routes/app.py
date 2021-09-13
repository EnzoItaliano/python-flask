from flask import Flask

app = Flask(__name__)

@app.route("/add/<int:a>/<int:b>")
def sum_route(a,b):
    result = a + b
    return f"{result}"

@app.route("/subtract/<int:a>/<int:b>")
def subtract_route(a,b):
    result = a - b
    return f"{result}"

@app.route("/multiply/<int:a>/<int:b>")
def multiply_route(a,b):
    result = a * b
    return f"{result}"

@app.route("/divide/<int:a>/<int:b>")
def divide_route(a,b):
    result = a / b
    return f"{result}"

@app.route("/math/<string:op>/<int:a>/<int:b>")
def math_route(op,a,b):
    result=""
    if op == 'add':
        result = a + b
    elif op == 'subtract':
        result = a - b
    elif op == 'multiply':
        result = a * b
    elif op == 'divide':
        result = a / b
    return f"{result}"