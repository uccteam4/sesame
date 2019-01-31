#Should work if using SQLAlchemy and a login form with these variables
#but can change things easily enough
#Testing is still to be done
from flask import Flask 
from flask_bcrypt import Bcrypt
from flaskblog import routes
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import login_user, current_user, logout_user

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        #Checks email instead of username
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            #If we decide to implement a remember me function
            login_user(user)#, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check e-mail and password')
    return render_template('login.html',title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
