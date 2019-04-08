# import the flask framework
import json
from flask import render_template
import requests
# needed to get requests to run on GAE
from requests_toolbelt.adapters import appengine
from . import mod_landing
# TODO: make the last commit more pretty


@mod_landing.route('/')
def index():
    # MAKE SURE TO CHANGE BEFORE PRODUCTION!!!!!!!!!!!!
    projects = requests.get("http://massoth.tech/updater/")
    projects = projects.json()
    print projects['projects']
    return render_template('landing/landing.html', projects=projects['projects'])
