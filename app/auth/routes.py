from flask import Flask
from app import db
from models import User
from app.auth import auth

@auth.route("/insert")
def insert():
    #r = Reasearcher("Pat","Den", "Pat_Den@mail.com", "operator","Dr.","Mr", "08611111", "+353", "0001")
    u = User("Elija")
    db.session.add(u)
    db.session.commit()

@auth.route("/query")
def query():
    rs = users.query.all()
    s = ""
    for r in rs:
        s += r.first_name + " " + r.email
    return s