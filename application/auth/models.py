from application import db
from application.models import BaseWithName

class Coach(BaseWithName):

    __tablename__ = "account"
    
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    teams = db.relationship("Team", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.points = 0

    def get_id(self):
        return self.id

    def is_active(self):
        return True
    
    def is_anonynmous(self):
        return False

    def is_authenticated(self):
        return True