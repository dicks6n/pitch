from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager


class User(UserMixin,db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(30), index = True)
    password_hash = db.Column(db.String(255))
    users = db.relationship('Pitch', backref = 'user_no', lazy = 'dynamic')
    email = db.Column(db.String(255), unique= True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    users_comments = db.relationship('Comments', backref="user_comments", lazy= "dynamic")
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
        
    @password.setter
    def password(self,password):
        self.password_hash= generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    def __repr__(self):
        return f'User {self.username}'
    
    from . import login_manager
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
       
class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(10))
    pitchname = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted= db.Column(db.DateTime,default=datetime.utcnow)
    pitch=db.relationship("Comments",backref="pitches_comments", lazy="dynamic")
    posted_by = db.Column(db.String())
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    
 
    
class Comments(db.Model):
    __tablename__= 'comments'
    
    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String)
    comment_title = db.Column(db.String)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    posted_by = db.Column(db.String())
    trial_test = db.Column(db.String())
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    
    
    