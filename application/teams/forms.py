from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class TeamForm(FlaskForm):
    name = StringField("Team name", [validators.Length(min=3)])
    race = StringField("Team race", [validators.Length(min=3)])
    resurrect = BooleanField("Resurrection team?")

    class Meta:
        csrf = False