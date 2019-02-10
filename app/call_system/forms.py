from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateTimeLocalField

class CallForm(FlaskForm):

    information = TextAreaField("Information", [InputRequired()])
    target_group = TextAreaField("Target Group", [InputRequired()])
    proposal_template = TextAreaField("Proposal Template", [InputRequired()])
    deadline = DateTimeLocalField("Deadline", format='%Y-%m-%dT%H:%M')