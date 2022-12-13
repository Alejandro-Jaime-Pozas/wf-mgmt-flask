from . import auth
from .http_auth import basic_auth, token_auth
from .models import *
from flask import jsonify, request

# routes for admin and employees...
# will need ability to:
# signup POST admin - normal admin signup form
@auth.route('/admins', methods=['GET', 'POST'])
def admin_signup():
    # need fname, lname, email, password attributes from frontend
    data = request.json
    # check if user has input all required fields, if not return err
    for field in {'first_name', 'last_name', 'email', 'password'}:
        if field not in data:
            return jsonify({'error': f'You are missing the {field} field.'}), 400
    # check if email value is unique, if not return err
    existing_user = \
        Admin.query.filter(Admin.email == data['email']).first() or \
        Employee.query.filter(Employee.email == data['email']).first()
    if existing_user:
        return jsonify({'error': f'''A user with the email {data['email']} already exists.'''}), 400
    # else all req fields have been included and there is no existing_user
    new_admin = Admin(**data)
    return jsonify(new_admin.to_dict())

# signup POST employee - admin needs to provide the employee's personal email and job title...
# login GET admin/employee
# update PUT admin/employee
# delete DELETE admin/employee

# GET all employees for a specific company/admin

# need to find way to create or pass some employee details from admin such as email and job title.
