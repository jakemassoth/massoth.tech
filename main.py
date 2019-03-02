from app.mod_github.controllers import mod_github as github_updater_module
from app.mod_landing.controllers import mod_landing as landing_module
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import instance.secrets as secrets
import sqlalchemy


app = Flask(__name__)

# configure database
SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{user}:{password}@localhost/{database}'
    '?unix_socket=/cloudsql/{connection_name}').format(
        user=secrets.DB_NAME, password=secrets.DB_PASS,
        database=secrets.DB_NAME, connection_name=secrets.CLOUD_SQL_CONNECTION_NAME)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

# General use 404 error handler
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# register modules
app.register_blueprint(landing_module)

app.register_blueprint(github_updater_module)
