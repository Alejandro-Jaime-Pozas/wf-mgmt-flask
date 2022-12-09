# include emplyee and admin users here
from app import db
import os, base64
from datetime import datetime, timedelta

# admin class is for admin person who handles employee onboarding mgmt. needs to have email/user, password, token access..

# TODO: admin class w methods
# TODO: employee class w methods

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = email # if future need for a username diff from email
    password = db.Column(db.String(128), nullable=False)
    token = db.Column(db.String(64), unique=True, index=True)
    token_expiration = db.Column(db.DateTime)
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    employees = db.relationship('Employee', backref='admin', lazy=True)


class Employee(Admin):
    employees = None