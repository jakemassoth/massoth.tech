from flask import Flask, render_template, request

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from mod_landing.controllers import mod_landing as landing_module

app.register_blueprint(landing_module)