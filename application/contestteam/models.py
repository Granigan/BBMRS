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
    def find_signed_teams_with_details(contest_id):
        stmt = text("SELECT team.id, team.name, team.race, account.name"
                    " FROM team, contestteam, account"
                    " WHERE contestteam.contest_id = :id" 
                    " AND contestteam.team_id = team.id" 
                    " AND account.id = team.account_id"
                    " ORDER BY team.name").params(id=contest_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "race":row[2], "coach":row[3]})

        return response
    
    @staticmethod
    def find_amount_of_teams_by_contest(contest_id):
        stmt = text("SELECT count(contestteam.id) FROM contestteam"
                    " WHERE contestteam.contest_id = :id").params(id=contest_id)
        res = db.engine.execute(stmt)

        
        for entry in res:
            response = entry

        return response


    @staticmethod
    def find_contests_by_team(team_id):
        stmt = text("SELECT contestteam.id FROM contestteam"
                    " WHERE contestteam.team_id = :id").params(id=team_id)
        res = db.engine.execute(stmt)

        response = []
        for entry in res:
            response.append(entry[0])

        return response

    @staticmethod
    def remove_all_teams_from_contest(contest_id):
        stmt = text("DELETE FROM contestteam"
                " WHERE contestteam.contest_id = :id").params(id=contest_id)
        db.engine.execute(stmt)

    @staticmethod
    def remove_team_from_all_contests(team_id):
        stmt = text("DELETE FROM contestteam"
                    " WHERE contestteam.team_id = :id").params(id=team_id)
        db.engine.execute(stmt)
