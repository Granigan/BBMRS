from application import app, db
from flask import redirect, render_template, request, url_for
from application.teams.models import Team
from application.teams.forms import TeamForm

@app.route("/teams", methods=["GET"])
def teams_index():
    return render_template("teams/list.html", teams = Team.query.all())

@app.route("/teams/new/")
def teams_form():
    return render_template("teams/new.html", form = TeamForm())

@app.route("/teams/add_point_<team_id>/", methods=["POST"])
def teams_add_point(team_id):

    t = Team.query.get(team_id)
    t.points = t.points + 1
    db.session().commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/subtract_point_<team_id>/", methods=["POST"])
def teams_subtract_point(team_id):

    t = Team.query.get(team_id)
    t.points = t.points - 1
    db.session().commit()

    return redirect(url_for("teams_index"))


@app.route("/teams/", methods=["POST"])
def teams_create():
    form = TeamForm(request.form)
    t = Team(name=form.name.data)
    t.race = form.race.data
    t.resurrect = form.resurrect.data
    t.coach = "user_id_here"
    

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("teams_index"))
