from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField 

class MatchForm(FlaskForm):
    winner = SelectField('Team', coerce=int)
    loser = SelectField('Team', coerce=int)

    def find_teams(self, teams):
        all_teams = []
        for team in teams:
            all_teams.append((team.id, team.name))
        self.winner.choices = all_teams
        self.loser.choices = all_teams

    class Meta:
        csrf = False

    