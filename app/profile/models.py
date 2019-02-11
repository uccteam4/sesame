from flask_sqlalchemy import SQLAlchemy

from app import db
from app.auth.models import User

class Researcher(db.Model):

    __tablename__ = "researchers"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable=False)
    job_title = db.Column(db.String, nullable=False)
    prefix = db.Column(db.String, nullable=False)

    suffix = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    phone_ext = db.Column(db.String, nullable=True)
    orcid = db.Column(db.String, nullable=True)

class Education(db.Model):

    __tablename__ = "education"

    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"),
                                                       primary_key=True)
    degree = db.Column(db.String, nullable=True)
    field_of_study = db.Column(db.String, nullable=True)
    institution = db.Column(db.String, nullable=True)
    location = db.Column(db.String, nullable=True)
    degree_award_year = db.Column(db.String, nullable=True)