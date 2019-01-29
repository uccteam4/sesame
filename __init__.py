import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=None
    )

    # if test_config is None:
    #     # load the instance of config, if it exists, when not testing
    #     app.config.from_pyfile("config.py", silent=True)
    # else:
    #     # load the test_config if its passed in
    #     app.config.from_mapping(test_config)
    app.config.from_mapping({"DATABASE":"///test.db"})

    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # A simple hello page
    @app.route("/")
    def hello():
        return "hello world"

    # Register the db with the app

    from . import db
    db.init_app(app)


    return app
