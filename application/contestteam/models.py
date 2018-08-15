from application import db
from application.models import Base
from sqlalchemy import text

class ContestTeam(Base):

    __tablename__ = "contestteam"

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    contest_id = db.Column(db.Integer, db.ForeignKey('contest.id'), nullable=False)

    def __init__(self, team_id, contest_id):
        self.team_id = team_id
        self.contest_id = contest_id

    @staticmethod
    def find_signed_teams():
        stmt = text("SELECT team.name FROM team, contestteam"
                    " WHERE contestteam.contest_id = 2 AND team.id = contestteam.team_id"
                    " ORDER BY team.name")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})

        return response