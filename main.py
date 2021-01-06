import os
from flask import Flask


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.add_url_rule('/', endpoint='index')

    return app
