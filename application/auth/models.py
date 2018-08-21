from application import db
from application.models import BaseWithName

class Coach(BaseWithName):

    __tablename__ = "account"
    
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    teams = db.relationship("Team", backref='account', lazy=True)

    def __init__(self, name, username, password, admin):
        self.name = name
        self.username = username
        self.password = password
        self.points = 0
        self.admin = admin

    def get_id(self):
        return self.id

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_admin(self):
        return self.admin
    
