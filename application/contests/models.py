from application import db
from application.models import BaseWithName
from application.auth.models import Coach

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
