from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import date

db=SQLAlchemy()

class Do(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  todo=db.Column(db.String(150),nullable=False)
  time=db.Column(db.Float,nullable=False)
  user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
  #goal_id=db.Column(db.Integer,db.ForeignKey('goal.id'))
  #goal=db.relationship('Goal',backref='do')
  

class Doday(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  time=db.Column(db.Float,nullable=False)
  date=db.Column(db.Date,default=date.today)
  

class Goal(db.Model):
  id=db.Column(db.Integer,primary_key=True,autoincrement=True)
  time=db.Column(db.Integer,default=0)
  user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

  
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    dos = db.relationship('Do', backref='user', lazy=True)
    goals = db.relationship('Goal', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
