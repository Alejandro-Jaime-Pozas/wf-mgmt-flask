# initiate the flask app, add cors, config, blueprints
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)