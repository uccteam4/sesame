from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Importing the db from main application module,
# may seperate it later to db.py module
from sesame import db

# Defining the base User
class User(db.Model):

    __abstact__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.email

# The Researcher
class Researcher(User):

    __tablename__ = "researchers"

    #id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    job_title = db.Column(db.String, nullable=False)
    prefix = db.Column(db.String, nullable=False)
    suffix = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    phone_ext = db.Column(db.String, nullable=True)
    orcid = db.Column(db.String, nullable=True)

    def __repr__(self):
        return "<User %r %r with ID %r>" % (self.first_name, self.last_name,
                                             self.id)


# The Admin
class Admin(User):

    __tablename__ = "admins"

class Education(db.Model):

    __tablename__ = "education"

    researcher_id = db.Column(db.Integer, ForeignKey("researcher.id",
                                                       primary_key=True))
    degree = db.Column(db.String, nullable=True)
    field_of_study = db.Column(db.String, nullable=True)
    institution = db.Column(db.String, nullable=True)
    location = db.Column(db.String, nullable=True)
    degree_award_year = db.Column(db.String, nullable=True)
