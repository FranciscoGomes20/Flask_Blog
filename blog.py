from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'loginUser'

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from app import routes, errors, models
