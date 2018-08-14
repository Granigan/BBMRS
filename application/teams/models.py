from application import db
from application.models import BaseWithName
from application.auth.models import Coach

class Team(BaseWithName):

    __tablename__ = "team"
    
    race = db.Column(db.String(144), nullable=False)
    resurrect = db.Column(db.Boolean, nullable=False)
    points = db.Column(db.Integer, nullable=False)

    # coach details
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.race = "missing"
        self.coach_name = "default"
        self.resurrect = 0
