# import the flask framework
import json
from flask import render_template
from . import mod_landing
import requests
# needed to get requests to run on GAE
from requests_toolbelt.adapters import appengine


@mod_landing.route('/')
def index():
    # MAKE SURE TO CHANGE BEFORE PRODUCTION!!!!!!!!!!!!
    projects = requests.get("http://localhost:8080/updater/")
    projects = projects.json()
    print projects['projects']
    return render_template('landing/landing.html', projects=projects['projects'])
