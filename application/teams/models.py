from application import db
from application.models import BaseWithName
from sqlalchemy.sql import text

class Team(BaseWithName):

    __tablename__ = "team"
    
    race = db.Column(db.String(144), nullable=False)
    resurrect = db.Column(db.Boolean, nullable=False)

    # coach details
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.race = "missing"
        self.resurrect = 0
    
    @staticmethod
    def find_teams_and_coaches():
        stmt = text("SELECT team.name, team.race,"
                    " team.resurrect, account.name, team.id"
                    " FROM team LEFT JOIN account ON account.id = account_id"
                    " ORDER BY team.name;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "race":row[1], "resurrect":row[2],
                "coach":row[3], "id":row[4]})

        return response

    @staticmethod
    def find_teams_by_coach(coach_id):

        stmt = text("SELECT team.id FROM team"
                    " WHERE team.account_id = :id").params(id=coach_id)

        res = db.engine.execute(stmt)
    
        response = []
        for entry in res:
            response.append(entry[0])

        return response
