from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    passw = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.Relationship('Note')