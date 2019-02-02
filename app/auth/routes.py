from flask import Flask
from app import db
from models import User, Researcher, Admin
from app.auth import auth

@auth.route("/insertr")
def insert():
    r1 = Researcher(name="Pat", orcid="0001")
    a1 = Admin(name="Tommy", position="Shell")
    r2 = Researcher(name="Chris", orcid="0002")
    a2 = Admin(name="Philip", position="supervisor")
    r3 = Researcher(name="Rachel", orcid="0003")
    db.session.add(r1)
    db.session.add(a1)
    db.session.add(r2)
    db.session.add(a2)
    db.session.add(r3)
    db.session.commit()
    return "successfully inserted!"



@auth.route("/query")
def query():
    # us = Researcher.query.all()
    # s = ""
    # for u in us:
    #     s += "Researcher: " + u.id + " " + u.first_name + " " + u.last_name + " " + u.email

    # us = Admin.query.all()
    # for u in us:
    #     s += "Admin: " + u.id + " " + u.first_name + " " + u.last_name + " " + u.
    
    # es = Employee.query.all()
    # s = ""
    # for e in es:
    #     s += "Employee: " + e.id + " " + e.name + e.title + "\n"

    es = User.query.all()
    s = ""
    for e in es:
        s += "User: " + str(e.id) + " " + e.account_type
        if e.account_type == "researcher":
            if e.name and e.orcid:
                s += " " + e.name + " " + e.orcid
        elif (e.account_type == "admin"):   
            if e.name and e.position:
                s += " " + e.name + " " + e.position
        s += "<br \>"

    return s