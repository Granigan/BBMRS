from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.contests.models import Contest
from application.contests.forms import ContestForm, TeamSignup
from application.contestteam.models import ContestTeam
from application.teams.models import Team

@app.route("/contests", methods=["GET"])
def contests_index():
    return render_template("contests/list.html", contests = Contest.find_contests_and_organisers())

@app.route("/contests/new/")
@login_required()
def contest_form():
    return render_template("contests/new.html", form=ContestForm())

@app.route("/contests", methods=["POST"])
@login_required()
def contest_create():
    form = ContestForm(request.form)

    if not form.validate():
        return render_template("contests/new.html", form=form)

    c = Contest(name=form.name.data, acronym=form.acronym.data, 
        maximum_slots=form.maximum_slots.data, resurrect=form.resurrect.data)
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("contests_index"))

@app.route("/contests/delete_<contest_id>", methods=['POST'])
@login_required(role="ADMIN")
def contest_delete(contest_id):
    
    for id in ContestTeam.find_contests_by_team(contest_id):
        ct = ContestTeam.query.get(id)
        db.session.delete(ct)
    
    db.session.commit()
    
    c = Contest.query.get(contest_id)

    db.session.delete(c)
    db.session.commit()

    return redirect(url_for("contests_index"))

@app.route("/contests/details_<contest_id>", methods=['GET'])
def contest_details(contest_id):
    c = Contest.query.get(contest_id)

    return render_template("contests/details.html", contest = c,
        contests = ContestTeam.find_signed_teams_with_details(contest_id))

@app.route("/contests/details_<contest_id>/signup")
@login_required()
def signup_form(contest_id):
    form = TeamSignup()
    form.find_user_teams(Team.query.all())

    return render_template("contestteam/new.html", contest_id = contest_id, form=form)

@app.route("/contests/details_<contest_id>", methods=['POST'])
@login_required()
def signed_up(contest_id):
    form = TeamSignup(request.form)
    ct = ContestTeam(team_id = form.user_teams.data, contest_id = contest_id)
    
    db.session.add(ct)
    db.session.commit()

    return redirect(url_for('contest_details', contest_id = contest_id))