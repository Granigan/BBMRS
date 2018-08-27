from application import db
from application.models import BaseWithName
from sqlalchemy.sql import text

class Coach(BaseWithName):

    __tablename__ = "account"
    
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144), nullable=False)

    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.points = 0
        self.role = role

    def get_id(self):
        return self.id

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True

    def get_role(self):
        return [self.role]
    
    @staticmethod
    def update_password(account_id, password):
        stmt = text("UPDATE account SET password = :pw WHERE id = :id"
                    ).params(pw=password, id=account_id)
        db.engine.execute(stmt)

