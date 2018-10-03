from .config import Production
from flask import Flask
from flask_bootstrap import Bootstrap
from .extension import db
from werkzeug.exceptions import RequestEntityTooLarge

def create_app(config=None):
    app = Flask(__name__)

    @app.errorhandler(413)
    def entity_too_large(error):
        return render_template_string('<html><h1>TOO LARGE!!</h1></html>'), 413

    # app.register_error_handler(RequestEntityTooLarge, entity_too_large)

    if config:
        app.config.from_object(config)
    else:
        app.config.from_object('config.Production')

    db.init_app(app)

    bootstrap = Bootstrap(app)

    return app

app = create_app(Production)
from .views import *
