from application import db
from application.models import BaseWithName

class Contest(BaseWithName):

    slots = db.Column(db.Integer)
    available_slots = db.Column(db.Integer)

    def __init__(self, name, slots):
        self.name = name
        self.slots = slots
        self.available_slots = slots

