from flask import Flask, render_template, abort

def create_app():
    app = Flask(__name__)

    # register modules
    from .mod_landing import mod_landing as landing_module

    app.register_blueprint(landing_module)

    # General use 404 error handler

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    return app
