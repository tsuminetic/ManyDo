from app import db
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    completed = db.Column(db.Boolean, default=False)
    #one to many
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))