from . import auth
from .http_auth import basic_auth, token_auth
from .models import *
from flask import jsonify, request

# routes for admin and employees...
# will need ability to:
# signup POST admin
# signup POST employee
# login GET admin/employee
# update PUT admin/employee
# delete DELETE admin/employee

# GET all employees for a specific company/admin

# need to find way to create or pass some employee details from admin such as email and job title.
