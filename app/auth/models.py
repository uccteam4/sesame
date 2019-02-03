from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy.ext.declarative import declared_attr

from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(256),unique=True)
    pwd_hash = db.Column(db.String(200))
    is_active = db.Column(db.Boolean,default=False)
    urole = db.Column(db.String(80))


    def __init__(self,username,email,pwd_hash,is_active,urole):
            self.email = email
            self.pwd_hash = pwd_hash
            self.is_active = is_active
            self.urole = urole     

class Researcher(db.Model):

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable=False)
    job_title = db.Column(db.String, nullable=False)
    prefix = db.Column(db.String, nullable=False)
    suffix = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    phone_ext = db.Column(db.String, nullable=True)
    orcid = db.Column(db.String, nullable=True)
