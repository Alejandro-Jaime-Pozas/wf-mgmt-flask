# include emplyee and admin users here
from app import db
import os, base64
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

# admin class is for admin person who handles employee onboarding mgmt. needs to have email/user, password, token access..
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
    employees = db.relationship('Employee', backref='admin', lazy=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs) # super to grab all of parent methods...+ new kwargs
        print(kwargs) # to check what kwargs is
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Admin|Email: {self.email}, Name: {self.first_name} {self.last_name}>"

    # method to get email domain for future use to create employee work emails
    def get_domain(self):
        return '@' + self.email.rsplit('@')[-1]

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
            # employees attribute add later
        }


# employee class is for new employees who go through onboarding process. need to confirm they're job offer, create std work email, 'link' their bank acct, choose their tech equipment. This class inherits from Admin parent class.
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    token = db.Column(db.String(64), unique=True, index=True)
    token_expiration = db.Column(db.DateTime)
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    job_title = db.Column(db.String(50)) # find way to make admin create employee's job title...
    personal_email = db.Column(db.String(100), unique=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False) # admin.id refers to admin table's id column
    bank_accounts = db.relationship('BankAcct', backref='employee', lazy=True)
    orders = db.relationship('Order', backref='employee', lazy=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs) # super to grab all of parent methods...+ new kwargs
        print(kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Employee|Email: {self.email}, Name: {self.first_name} {self.last_name}>"

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_token(self, expires_in=3600): # COME BACK
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(minutes=1): # this checks to see if there is an existing token for user
            return self.token
        self.token = base64.b64encode(os.urandom(16)).decode('utf-8') # this is gibberish
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.commit()
        return self.token

    def update(self, data): # COME BACK
        pass

    # create a json type object
    def to_dict(self): 
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'job_title': self.job_title,
            'personal_email': self.personal_email,
            'create_date': self.create_date,
            'active': self.active,
            # bank accts, orders add? or add employee to BankAccount, Order classes?
        }
