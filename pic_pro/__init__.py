
from flask import Flask
from flask_bootstrap import Bootstrap
from .extension import db
from .config import Production

def create_app(config=None):
    app = Flask(__name__)

    if config:
        app.config.from_object(config)
    else:
        app.config.from_object('config.Production')

    db.init_app(app)

    bootstrap = Bootstrap(app)

    return app

app = create_app(Production)
