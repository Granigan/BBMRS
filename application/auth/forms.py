from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    coach_name = StringField("Coach name", [validators.Length(min=4)])
    username = StringField("Username", [validators.Length(min=4)])
    password = PasswordField("Password", [validators.Length(min=4)])
    role = SelectField('User role',choices=[("COACH", "Coach"), ("ADMIN", "Admin")])

    class Meta:
        csrf = False

class ChangePasswordForm(FlaskForm):
    password = PasswordField("New password")

    class Meta:
        csrf = False