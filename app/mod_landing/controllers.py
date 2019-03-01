"""`main` is the top level module for your Bottle application."""

# import the flask framework
from flask import Blueprint, render_template, request
import json

filename = 'response.json'

mod_landing = Blueprint(
    'mod_landing', __name__, url_prefix="/", template_folder='../templates')

with open(filename, 'r') as f:
    projects = json.load(f)


@mod_landing.route('/')
def index():
    return render_template('landing/landing.html', projects=projects)
