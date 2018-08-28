from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators, SelectField

class ContestForm(FlaskForm):
    name = StringField("Contest name", [validators.Length(min=5)])
    acronym = StringField("Acronym", [validators.Length(min=2)])
    maximum_slots = IntegerField("Amount of teams", [validators.NumberRange(min=2)])
    resurrect = BooleanField("Resurrection rules?")

    class Meta:
        csrf = False

class TeamSignup(FlaskForm):
    user_teams = SelectField('Team', coerce=int)

    def find_user_teams(self, teams):
        self.user_teams.choices = teams

    class Meta:
        csrf = False
