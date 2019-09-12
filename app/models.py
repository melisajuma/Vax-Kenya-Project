from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from sqlalchemy import func
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'mothers'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100),unique = True,index = True)
    # id_no = db.Column(db.Integer(8),db.ForeignKey("mothers.id"))
    # password_hash = db.Column(db.String(100))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    # child = db.relationship('Child', backref = 'user',lazy = 'dynamic')
    password = db.Column(db.String(100))
    # vaccine = db.relationship('Vaccine',backref = 'user',lazy = 'dynamic')
    
    @property
    def password(self, password):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)
    def __repr__(self):
        return f'User {self.username}'


class Child(db.Model):
    __tablename__ = 'child'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    DoB = db.Column(db.Integer())
    
    # vaccine = db.relationship('vaccine', backref = 'child',lazy = 'dynamic')
    def save_child(self):
        db.session.add(self)
        db.session.commit()
    def get_child(self):
        child = Child.query.all()
        return child 
@login_manager.user_loader
def load_user(username):
    return User.query.get(int(username))      
