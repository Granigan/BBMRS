from application import db
from application.models import Base

class Match(Base):

    __tablename__ = "match"
    
    winner_id = db.Column(db.Integer, nullable=False)
    loser_id = db.Column(db.Integer, nullable=False)

    def __init__(self, winner_id, loser_id):
        self.winner_id = winner_id
        self.loser_id = loser_id

