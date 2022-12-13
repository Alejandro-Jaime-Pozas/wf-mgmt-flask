from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from .models import *
from datetime import datetime

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

# check password for admin and employee
@basic_auth.verify_password
def verify(email, password):
    user = Admin.query.filter_by(email=email).first() or Employee.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    # employee = Employee.query.filter_by(email=email).first()
    # if employee and employee.check_password(password):
    #     return employee

@token_auth.verify_token
def verify(token):
    user = Admin.query.filter_by(token=token).first() or Employee.query.filter_by(token=token).first()
    now = datetime.utcnow()
    if user and user.token_expiration > now:
        return user