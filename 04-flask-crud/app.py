from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from snack import Snack

app = Flask(__name__)
snack_list = []

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route("/snacks", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        kind = request.form['kind']
        snack_list.append(Snack(name, kind))
    return render_template('snacks.html', snacks=snack_list)

@app.route("/snacks/new")
def add_snack():
    return render_template('add-snack.html')

@app.route("/snacks/<int:id>", methods=['POST', 'GET'])
def show_snack(id):
    index_snack = -1
    for index, snack in enumerate(snack_list):
        if snack.id == id:
            index_snack = index
    if 'PATCH' in str(request.query_string):
        snack_list[index_snack].name = request.form['name']
        snack_list[index_snack].kind = request.form['kind']
        return redirect(url_for('index'))
    elif 'DELETE' in str(request.query_string):
        snack_list.remove(snack_list[index_snack])
        return redirect(url_for('index'))
    
    return render_template('snack.html', snack=snack_list[index_snack])

@app.route("/snacks/<int:id>/edit")
def update_snack(id):
    index_snack = -1
    for index, snack in enumerate(snack_list):
        if snack.id == id:
            index_snack = index
    return render_template('edit-snack.html', snack=snack_list[index_snack])