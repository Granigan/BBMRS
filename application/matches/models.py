from application import db

class Match(db.Model):

    __tablename__ = "match"
    
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    #winning team id
    winner = db.Column(db.Integer, nullable=False)
    #losing team id
    loser = db.Column(db.Integer, nullable=False)

    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser

