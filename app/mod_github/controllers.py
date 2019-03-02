from flask import Blueprint
from models import Projects
mod_github = Blueprint(
    'mod_github', __name__, url_prefix="/updater", template_folder='../templates')


@mod_github.route('/')
def update():
    pass
