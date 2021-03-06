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

# login
from application.auth.models import Coach
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in to use this functionality."

# user roles
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.get_role():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# application functionality
from application import views

from application.teams import models
from application.teams import views

from application.auth import models
from application.auth import views

from application.contests import models
from application.contests import views

from application.contestteam import models

from application.matches import models
from application.matches import views

@login_manager.user_loader
def load_coach(coach_id):
    return Coach.query.get(coach_id)

# db creation
try:
    db.create_all()
except:
    pass
