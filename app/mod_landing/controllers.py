# import the flask framework
import json
from flask import render_template
from . import mod_landing


filename = 'response.json'

with open(filename, 'r') as f:
    projects = json.load(f)


@mod_landing.route('/')
def index():
    return render_template('landing/landing.html', projects=projects)
