# Import Flask
from flask import Flask, render_template, flash, redirect, url_for

# Import the extensions used here
from app import db, login_manager
import app.call_system.forms
from flask_login import current_user, login_required

# Import call_system blueprint
from app.call_system import call_system

# Import the Models used
from app.call_system.models import Call

# Import the forms
from app.call_system.forms import CallForm

import datetime
@call_system.route("/make_call", methods=["GET", "POST"])
@login_required
def make_call():
    form = CallForm()
    if form.is_submitted():
        if form.validate():
            # render a new page which confirms the call??
            # two step process like asking a question on stack overflow
            
            # check they are admin
            # Obtain all info, make a new Call object,
            # Render a new page that is a confirmation of input
            # or simply insert the call into the database
            # 
            # Publishing stuff may also be trigered? its a backgrond job?
            call = Call(published_by=current_user.id, information=form.information.data,
                        target_group=form.target_group.data, proposal_template=form.proposal_template.data,
                        deadline=form.deadline.data)
            db.session.add(call)
            db.session.commit()

            flash("Call for funding has been published")
            return render_template("call_system/make_call.html", form=form) 
        else:
            #flash(str(form.errors))
            flash("Unable to publish call - Please enter details in all fields")
            return render_template("call_system/make_call.html", form=form)
    else:
        return render_template("call_system/make_call.html", form=form)

@call_system.route("/query")
def query():
    calls = Call.query.all()
    return str(len(calls))

@call_system.route("/user")
def user():
    u = current_user
    return str(current_user)