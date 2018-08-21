from application import db
from application.models import BaseWithName
from application.auth.models import Coach
from sqlalchemy.sql import text

class Contest(BaseWithName):

    acronym = db.Column(db.String(144), nullable=False)
    number_of_teams = db.Column(db.Integer)
    maximum_slots = db.Column(db.Integer, nullable=False)
    resurrect = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, acronym, maximum_slots, resurrect):
        self.name = name
        self.acronym = acronym
        self.number_of_teams = 0
        self.maximum_slots = maximum_slots
        self.resurrect = resurrect

    @staticmethod
    def find_contests_and_organisers():
        stmt = text("SELECT contest.name, contest.acronym, contest.resurrect,"
                    " contest.number_of_teams, contest.maximum_slots, account.name, contest.id"
                    " FROM contest LEFT JOIN account ON account.id = account_id"
                    " ORDER BY contest.name")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "acronym":row[1], "resurrect":row[2],
            "teams":row[3], "slots":row[4], "organiser":row[5], "id":row[6]})

        return response

    @staticmethod
    def find_contests_by_coach(coach_id):
        stmt = text("SELECT contest.id FROM contest"
                    " WHERE contest.account_id = :id").params(id=coach_id)

        res = db.engine.execute(stmt)
        
        response = []

        for entry in res:
            response.append(entry[0])

        return response
