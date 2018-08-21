from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, login_required
from application.auth.models import Coach
from application.auth.forms import LoginForm, RegisterForm
from application.teams.models import Team
from application.contestteam.models import ContestTeam
from application.contests.models import Contest

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    coach = Coach.query.filter_by(username=form.username.data, 
    password=form.password.data).first()
    if not coach:
        return render_template("auth/loginform.html", form = form,
            error = "No such username or password.")

    login_user(coach)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("/auth/registerform.html", form = RegisterForm())
    
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    c = Coach(name = form.coach_name.data, username = form.username.data, 
        password = form.password.data, role=form.role.data)
    
    db.session.add(c)
    db.session.commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/accounts", methods=["GET"])
@login_required(role="ADMIN")
def accounts_index():
    return render_template("auth/list.html", accounts = Coach.query.all())

@app.route("/auth/account_<account_id>", methods=["GET"])
@login_required(role="ADMIN")
def account_details(account_id):
    a = Coach.query.get(account_id)

    return render_template("auth/details.html", account = a)

@app.route("/auth/delete_account_<account_id>", methods=['POST'])
@login_required(role="ADMIN")
def account_delete(account_id):
    # remove teams from contests and delete them
    for team_id in Team.find_teams_by_coach(account_id):
        ContestTeam.remove_team_from_all_contests(team_id)
        t = Team.query.get(team_id)
        db.session.delete(t)
        db.session.commit()

    # empty and delete contests
    for contest_id in Contest.find_contests_by_coach(account_id):
        print("\n\n seeking contest id: " + str(contest_id))
        ContestTeam.remove_all_teams_from_contest(contest_id)
        c = Contest.query.get(contest_id)
        db.session.delete(c)
        db.session.commit()

    # delete account
    c = Coach.query.get(account_id)
    db.session.delete(c)
    db.session.commit()

    return redirect(url_for("accounts_index"))

