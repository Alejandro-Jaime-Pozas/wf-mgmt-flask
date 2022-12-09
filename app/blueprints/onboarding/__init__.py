from flask import Blueprint

onboarding = Blueprint('onboarding', __name__, url_prefix='/onboarding')

from . import models, routes