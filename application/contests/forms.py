from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class ContestForm(FlaskForm):
    name = StringField("Contest name", [validators.Length(min=5)])
    acronym = StringField("Acronym", [validators.Length(min=2)])
    maximum_slots = IntegerField("Amount of teams", [validators.NumberRange(min=2)])
    resurrect = BooleanField("Resurrection rules?")

    class Meta:
        csrf = False
