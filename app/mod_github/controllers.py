import dateutil.parser
from ..models import Project, ProjectSchema
from .. import db
from . import mod_github
from flask import jsonify
import requests
# needed to get requests to run on GAE
from requests_toolbelt.adapters import appengine

# monkey patch requests to support GAE
appengine.monkeypatch()


@mod_github.route('/')
def get_data():
    """ an endpoint that returns the current github projects in the database, ordered by the last commit, i.e. the project with the most recent commit is first"""
    query = Project.query.order_by(Project.last_commit.desc()).all()
    project_schema = ProjectSchema(many=True)
    data = project_schema.dump(query).data
    return jsonify({"projects": data})

# TODO: add validation of GAE cron header
# TODO: add Github api rate limiting error handling
# TODO: general error handling
@mod_github.route('/run')
def run_updater():
    """ an endpoint to update the github project database, only intended to run 60 times a day using the GAE cron interface, more than this will lead to being locked out by the github API. Deletes all rows in the table and then re-populates them with the new data"""
    db.session.query(Project).delete()
    db.session.commit()
    resp = requests.get("https://api.github.com/users/bluzomby/repos")
    for item in resp.json():
        project = Project(name=item['name'], description=item['description'], last_commit=dateutil.parser.parse(item['updated_at']),
                          stars=item['stargazers_count'], forks=item['forks_count'], language=item['language'], url=item['html_url'])
        db.session.add(project)
    db.session.commit()
    return jsonify({"result": "success"})
