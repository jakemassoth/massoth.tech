from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import instance.secrets as secrets

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    # configure database
    # PRODUCTION ONLY
    # SQLALCHEMY_DATABASE_URI = (
    #     'mysql+pymysql://{user}:{password}@localhost/{database}'
    #     '?unix_socket=/cloudsql/{connection_name}').format(
    #         user=secrets.DB_USER, password=secrets.DB_PASS,
    #         database=secrets.DB_NAME, connection_name=secrets.CLOUD_SQL_CONNECTION_NAME)
    # # dev database connection setup
    app.config['SQLALCHEMY_DATABASE_URI'] = secrets.SQLALCHEMY_DATABASE_URI
    db.init_app(app)

    ma.init_app(app)

    # register modules
    from .mod_landing import mod_landing as landing_module

    app.register_blueprint(landing_module)

    from .mod_github import mod_github as github_updater_module

    app.register_blueprint(github_updater_module, url_prefix="/updater")

    # General use 404 error handler

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    return app
