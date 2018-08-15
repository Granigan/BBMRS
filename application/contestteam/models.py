from application import db
from application.models import Base

class ContestTeam(Base):

    __tablename__ = "contestteam"

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    contest_id = db.Column(db.Integer, db.ForeignKey('contest.id'), nullable=False)

    def __init__(self, team_id, contest_id):
        self.team_id = team_id
        self.contest_id = contest_id
