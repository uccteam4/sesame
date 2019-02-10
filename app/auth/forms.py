from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    email = StringField("Email")
    password = PasswordField("Password")

class RegistrationForm(FlaskForm):
    email = StringField("Email", [InputRequired()])
    password = PasswordField("Password", [InputRequired()])

    first_name = StringField("First name", [InputRequired()])
    last_name = StringField("Last name", [InputRequired()])
    job_title = StringField("Job title", [InputRequired()])
    prefix = StringField("Prefix", [InputRequired()])

    suffix = StringField("Suffix")
    phone = IntegerField("Phone")
    phone_ext = IntegerField("Phone Extension")
    orcid = StringField("Orcid")

#temporary class for a temp call for proposals form
#used to test email notification functionality
class CallForProposalsForm(FlaskForm):
    proposal_name = StringField("Proposal Name", [InputRequired()])
    
