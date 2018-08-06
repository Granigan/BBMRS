from application import db
from application.coaches.models import Coach

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    race = db.Column(db.String(144), nullable=False)
    resurrect = db.Column(db.Boolean, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    coach_name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.race = "missing"
        self.coach_name = "default"
        self.resurrect = 0

