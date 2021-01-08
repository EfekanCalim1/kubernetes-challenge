from application import db

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(255), nullable=False)
    review = db.relationship('Review', backref='players')
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(255))
    players_id = db.Column(db.Integer, db.ForeignKey('players.id'))
