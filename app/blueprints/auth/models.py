# include emplyee and admin users here
from app import db
import os, base64
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

# admin class is for admin person who handles employee onboarding mgmt. needs to have email/user, password, token access..

# TODO: admin class w methods
# TODO: employee class w methods

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    token = db.Column(db.String(64), unique=True, index=True)
    token_expiration = db.Column(db.DateTime)
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    # employees = db.relationship('Employee', backref='admin', lazy=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs) # super to grab all of parent methods...+ new kwargs
        print(kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Admin|Email: {self.email}, Name: {self.first_name} {self.last_name}>"

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_token(self, expires_in=3600): # COME BACK
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(minutes=1): # this checks to see if there is an existing token for user
            return self.token
        self.token = base64.b64encode(os.urandom(16)).decode('utf-8') # this is gibberish
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.commit() # why no db.session.add??
        return self.token

    def delete(self):
        db.session.delete(self) # it seems like delete is a fn from the db.session module...
        db.session.commit()

    def update(self, data): # COME BACK
        pass

    # create a json type object
    def to_dict(self): 
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'create_date': self.create_date,
            'active': self.active,
            # employees attribute add
        }
