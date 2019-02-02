from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy.ext.declarative import declared_attr

from app import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    account_type = db.Column("type", db.String)

    __mapper_args__ = {"polymorphic_on": account_type}

    # def __init__(self, name):
    #     self.name = name

    def __repr__(self):
        return "user %i %s" % (self.id, self.name)

class Researcher(User):
    __mapper_args__ =  {'polymorphic_identity': 'researcher'}
    
    @declared_attr
    def name(cls):
        return User.__table__.c.get("name", db.Column(db.String))

    orcid = db.Column(db.String)

    # def __init__(self, name, orcid):
    #     User.__init__(self, name)
    #     self.self = orcid


class Admin(User):
    __mapper_args__ =  {'polymorphic_identity': 'admin'}
    
    @declared_attr
    def name(cls):
        return User.__table__.c.get("name", db.Column(db.String))

    position = db.Column(db.String)

    # def __init__(self, name, position):
    #     User.__init__(self, name)
    #     self.position = position



# #The Researcher
# class Researcher(IdModel):

#     __tablename__ = "researchers"
#     __abstact__ = False
    
#     first_name = db.Column(db.String, nullable=False)
#     last_name = db.Column(db.String, nullable = False)
#     email = db.Column(db.String, nullable = False)
#     job_title = db.Column(db.String, nullable=False)
#     prefix = db.Column(db.String, nullable=False)
#     suffix = db.Column(db.String, nullable=True)
#     phone = db.Column(db.String, nullable=True)
#     phone_ext = db.Column(db.String, nullable=True)
#     orcid = db.Column(db.String, nullable=True)

#     def __init__(self, first_name, last_name, email, job_title, prefix, suffix, phone, phone_ext, orcid):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.prefix = prefix
#         self.suffix = suffix
#         self.phone = phone
#         self.phone_ext = phone_ext
#         self.orcid = orcid

#     def __repr__(self):
#        return "<User %r %r with ID %r>" % (self.first_name, self.last_name,
#                                             self.id)

# class Admin(IdModel):

#     __tablename__ = "admins"

#     first_name = db.Column(db.String, nullable=False)
#     last_name = db.Column(db.String, nullable = False)
#     email = db.Column(db.String, nullable = False)

#     def __init__(self, first_name, last_name, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email

# class Education(db.Model):

#     __tablename__ = "education"

#     researcher_id = db.Column(db.Integer, db.ForeignKey("researcher.id",
#                                                        primary_key=True))
#     degree = db.Column(db.String, nullable=True)
#     field_of_study = db.Column(db.String, nullable=True)
#     institution = db.Column(db.String, nullable=True)
#     location = db.Column(db.String, nullable=True)
#     degree_award_year = db.Column(db.String, nullable=True)
