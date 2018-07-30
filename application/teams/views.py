from application import app, db
from flask import redirect, render_template, request, url_for
from application.teams.models import Team

@app.route("/teams", methods=["GET"])
def teams_index():
    return render_template("teams/list.html", teams = Team.query.all())

@app.route("/teams/new/")
def teams_form():
    return render_template("teams/new.html")

@app.route("/teams/<team_id>/", methods=["POST"])
def teams_add_point(team_id):

    t = Team.query.get(team_id)
    t.points = t.points + 1
    db.session().commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/", methods=["POST"])
def teams_create():
    t = Team(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("teams_index"))
