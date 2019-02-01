# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlcheny
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../config.py")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from app.auth import auth
    app.register_blueprint(auth, url_prefix="/auth/")

    return app