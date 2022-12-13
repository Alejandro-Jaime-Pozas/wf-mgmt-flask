from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from .models import *
from datetime import datetime

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

# verify password for admin or employee
@basic_auth.verify_password
def verify(email, password):
    # CHECK TO SEE IF CODE BELOW WORKS..
    user = Admin.query.filter_by(email=email).first() or Employee.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    # employee = Employee.query.filter_by(email=email).first()
    # if employee and employee.check_password(password):
    #     return employee

# verify a token for admin or employee
@token_auth.verify_token
def verify(token):
    user = Admin.query.filter_by(token=token).first() or Employee.query.filter_by(token=token).first()
    now = datetime.utcnow()
    if user and user.token_expiration > now:
        return user