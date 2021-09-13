from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "<p>welcome</p>"

@app.route("/welcome/home")
def welcome_home():
    return "<p>welcome home</p>"

@app.route("/welcome/back")
def welcome_back():
    return "<p>welcome back</p>"

@app.route("/sum")
def sum_route():
    sum = 5 + 5
    return f"{sum}"