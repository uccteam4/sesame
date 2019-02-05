from flask_sqlalchemy import SQLAlchemy
import datetime

from app import db
import app.profile.models


class Call(db.Model):

    __tablename__ = "calls"

    # Meta information about the call
    id = db.Column(db.Integer, primary_key=True)
    date_published = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    published_by = db.Column(db.Integer, db.ForeignKey("admins.user_id"))

    # Actual content of the call
    information = db.Column(db.String)
    target_group = db.Column(db.String)
    proposal_template = db.Column(db.String)
    deadline = db.Column(db.DateTime)

    # The applications associated with the call
    #applications = db.Column(db.relationship("app.call_system.models.Application"))

class Application():
    # Temporary class for the application model. 
    # Will be done when doing the application system

    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)

    #call = relationship("app.call_system.models.Call", back_populates="applications")