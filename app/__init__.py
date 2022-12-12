# initiate the flask app, add cors, config, blueprints
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)

# init config for flask app using Config class variables
app.config.from_object(Config)

# init cross origin resource sharing
CORS(app)

# init sql database using sqlalchemy
db = SQLAlchemy(app)

# init migrate to allow db creation and updating
migrate = Migrate(app, db)

# import blueprints here after initializing other fns so app can function
from .blueprints.auth import auth
app.register_blueprint(auth)
from .blueprints.onboarding import onboarding
app.register_blueprint(onboarding)

# import routes after initializing other fns
from . import routes