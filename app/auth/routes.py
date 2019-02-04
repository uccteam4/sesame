# Import Flask
from flask import Flask, render_template, flash, redirect, url_for

# Import the extensions used here
from app import db, bcrypt, login_manager
from app.auth.forms import LoginForm, RegistrationForm
from flask_login import UserMixin, current_user, login_user, logout_user

# Import auth blueprint
from app.auth import auth

# Import the Models used
from app.profile.models import Researcher
from app.profile.models import User


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:

            password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            user = User(form.email.data, password, "RESEARCHER")
            db.session.add(user)
            db.session.commit()
            
            user = User.query.filter_by(email=form.email.data).first()
            researcher = Researcher(user_id=user.id, first_name=form.first_name.data, last_name=form.last_name.data,
                                     job_title=form.job_title.data, prefix=form.prefix.data, suffix=form.suffix.data, 
                                     phone=form.phone.data, phone_ext=form.phone_ext.data, orcid=form.orcid.data)
            db.session.add(researcher)
            education = Education(user_id=user.id, degree=None, field_of_study=None, institution=None,
                                    location=None,degree_award_year=None)
            db.session.add(education)
            db.session.commit()

            flash("Your account has been created. You can now login")
            return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        #Checks email instead of username
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.pwd_hash,form.password.data):
            #If we decide to implement a remember me function
            login_user(user)#, remember=form.remember.data)
            flash("You are now logged in")
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check e-mail and password')
    return render_template('auth/login.html',title='Login', form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@auth.route("/query")
def query():
    users = User.query.all()
    return str(len(users))
