from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/person/<name>/<age>")
def person(name, age):
    return render_template('base.html', name=name, age=age)

@app.route("/math")
def math_route():
    a = int(request.args.get('num1'))
    b = int(request.args.get('num2'))
    op = request.args.get('calculation')
    result=""
    if op == 'add':
        result = a + b
    elif op == 'subtract':
        result = a - b
    elif op == 'multiply':
        result = a * b
    elif op == 'divide':
        if b == 0: return "Please do not divide by 0"
        result = a / b
    return f"{result}"

@app.route("/calculate", methods=['POST', 'GET'])
def calculate():
    if request.method == 'POST':
        a = request.form['num1']
        b = request.form['num2']
        op = request.form['calculation']
        return redirect(url_for('math_route', num1=a, num2=b, calculation=op))
    return render_template('calc.html')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def result():
    keyword = request.args.get('keyword')
    url = 'https://news.google.com'
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    titles = soup.find_all('a', {'class': 'RZIKme'})
    articles = [{
        'title': title.text,
        'link': f"{url}{title.get('href')[1:]}"
    } for title in titles]

    matching_articles = [
        article 
        for article in articles
        if keyword.lower() in article['title'].lower()
    ]
    return render_template('results.html', articles=matching_articles)