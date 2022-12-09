from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import models, routes, http_auth