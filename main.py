"""`main` is the top level module for your Bottle application."""

# import the flask framework
from flask import Flask, render_template, request
import json

filename = 'response.json'

with open(filename, 'r') as f:
    projects = json.load(f)
app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/')
def index():
    return render_template('projects.html', projects=projects)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404