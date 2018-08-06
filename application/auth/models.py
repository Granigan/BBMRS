from application import db

class Coach(db.Model):

    __tablename__ = "account"
    
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

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

