from application import db

class Contest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)
    slots = db.Column(db.Integer)
    available_slots = db.Column(db.Integer)

    def __init__(self, name, slots):
        self.name = name
        self.slots = slots
        self.available_slots = slots

