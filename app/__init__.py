from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Application
app = Flask(__name__)
app.config.from_object(Config)

# Login in application
login = LoginManager(app)
login.login_view = 'login'

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
