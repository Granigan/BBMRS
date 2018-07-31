from application import db

class Coach(db.Model):

    __tablename__ = "account"
    
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
        self.points = 0

