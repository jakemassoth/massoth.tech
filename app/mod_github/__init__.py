from flask import Blueprint
mod_github = Blueprint(
    'mod_github', __name__, template_folder='../templates')
from . import controllers