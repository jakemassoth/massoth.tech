# import the flask framework
import json
from flask import render_template
import requests
# needed to get requests to run on GAE
from requests_toolbelt.adapters import appengine
from . import mod_landing


@mod_landing.route('/')
def index():
    projects = requests.get("https://api.github.com/users/jakemassoth/repos")
    if projects.ok:
        projects = projects.json()
        projects = sorted(projects, key=lambda x: x['updated_at'], reverse=True)
    else:
        projects = json.dumps({
            "name": "",
            "language": "",
            "description": "",
            "stargazers_count": "",
            "forks_count": "",
            "updated_at": "",
        })

    return render_template('landing/landing.html', projects=projects)
