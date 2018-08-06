from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class TeamForm(FlaskForm):
    name = StringField("Team name")
    race = StringField("Team race")
    resurrect = BooleanField("Resurrection team?")

    class Meta:
        csrf = False