from application import db
from application.models import Base
from sqlalchemy import text


class Match(Base):

    __tablename__ = "match"
    
    winner_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    loser_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __init__(self, winner_id, loser_id):
        self.winner_id = winner_id
        self.loser_id = loser_id

    @staticmethod
    def find_match_history(team_id):
        stmt = text("SELECT m.date_created AS date, w.name AS winner, l.name AS loser"
                    " FROM match AS m"
                    " LEFT JOIN team AS w ON m.winner_id = w.id"
                    " LEFT JOIN team AS l ON m.loser_id = l.id"
                    " WHERE m.winner_id = :id OR m.loser_id = :id order by date").params(id=team_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"date":row[0], "winner":row[1], "loser":row[2]})
        
        return response

    @staticmethod
    def find_total_games_played_by_team(team_id):
        stmt = text("SELECT count(id) FROM match"
                    " WHERE winner_id = :id OR loser_id = :id").params(id=team_id)

        res = db.engine.execute(stmt)
        response = []

        for entry in res:
            response.append(entry[0])

        if(len(response)==0):  
            response.append(0)

        return response
    
    @staticmethod
    def delete_match_history(team_id):
        stmt = text("DELETE FROM match"
                    " WHERE winner_id = :id OR loser_id = :id").params(id=team_id)
        db.engine.execute(stmt)

    @staticmethod
    def find_wins_by_team(team_id):
        stmt = text("SELECT count(id) FROM match"
                    " WHERE winner_id = :id ").params(id=team_id)
        
        res = db.engine.execute(stmt)
        response = []        

        for entry in res:
            response.append(entry[0])

        if(len(response)==0):  
            response.append(0)

        return response

    @staticmethod
    def find_losses_by_team(team_id):
        stmt = text("SELECT count(id) FROM match"
                    " WHERE loser_id = :id ").params(id=team_id)
        
        res = db.engine.execute(stmt)
        response = []

        for entry in res:
            response.append(entry[0])

        if(len(response)==0):  
            response.append(0)

        return response
    
    @staticmethod
    def find_win_percentage_by_team(team_id):
        stmt = text("SELECT (count(winner_id)* 100.0 /"
                    " (SELECT count(*) FROM match"
                    " WHERE winner_id = :id OR loser_id = :id))"
                    " FROM match WHERE winner_id = :id").params(id=team_id)
        
        res = db.engine.execute(stmt)

        response = []

        for entry in res:
            response.append(entry[0])

        return response

