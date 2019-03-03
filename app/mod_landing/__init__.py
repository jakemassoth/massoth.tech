from flask import Blueprint
mod_landing = Blueprint(
    'mod_landing', __name__, template_folder='../templates')
from . import controllers
