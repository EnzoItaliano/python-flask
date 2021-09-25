from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from db import create_snack, create_table, edit_snack, find_all_snacks, find_snack, remove_snack

app = Flask(__name__)
create_table()

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route("/snacks", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        kind = request.form['kind']
        create_snack(name, kind)
    snack_list = find_all_snacks()
    return render_template('snacks.html', snacks=snack_list)

@app.route("/snacks/new")
def add_snack():
    return render_template('add-snack.html')

@app.route("/snacks/<int:id>", methods=['POST', 'GET'])
def show_snack(id):
    resp = find_snack(id)
    if '_method=PATCH' in str(request.query_string):
        name = request.form['name']
        kind = request.form['kind']
        edit_snack(name,kind,id)
        return redirect(url_for('index'))
    elif '_method=DELETE' in str(request.query_string):
        remove_snack(id)
        return redirect(url_for('index'))
    
    return render_template('snack.html', snack=resp)

@app.route("/snacks/<int:id>/edit")
def update_snack(id):
    resp = find_snack(id)
    return render_template('edit-snack.html', snack=resp)