from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func


#creating db model for the users containing id, email, passw, name and notes showing the relationship between users model and the notes model 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    passw = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.Relationship('Note')

    
#creating db model for the notes which contains id, note, date created and the users id who wrote the note using a foreign key
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.Date)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))



