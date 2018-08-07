from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

# db config
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///teams.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# application functionality
from application import views

from application.teams import models
from application.teams import views

from application.auth import models
from application.auth import views

from application.contests import models
from application.matches import models

# login
from application.auth.models import Coach
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in to use this functionality."

@login_manager.user_loader
def load_coach(coach_id):
    return Coach.query.get(coach_id)

# db creation
try:
    db.create_all()
except:
    pass
