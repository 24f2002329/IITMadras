from . import db   # here '.' means the __init__.py file in the same directory
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(50))
    quizzes = db.relationship('Quiz', backref='author', lazy=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow().date())
    updated_date = db.Column(db.DateTime, default=datetime.utcnow().date())

# class Quiz(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150))
#     questions = db.relationship('Question', backref='quiz', lazy=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     created_date = db.Column(db.DateTime, default=datetime.utcnow().date())
#     updated_date = db.Column(db.DateTime, default=datetime.utcnow().date())

