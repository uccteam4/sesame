# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlcheny
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../config.py")

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.auth import auth
    app.register_blueprint(auth, url_prefix="/auth/")
    from app.profile import profile
    app.register_blueprint(profile)

    with app.app_context():
        db.create_all()

    return app
