from application import db
from application.models import Base

class Match(Base):

    __tablename__ = "match"
    
    #winning team id
    winner = db.Column(db.Integer, nullable=False)
    #losing team id
    loser = db.Column(db.Integer, nullable=False)

    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser

