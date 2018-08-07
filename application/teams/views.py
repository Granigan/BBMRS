from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.teams.models import Team
from application.teams.forms import TeamForm

@app.route("/teams", methods=["GET"])
def teams_index():
    return render_template("teams/list.html", teams = Team.query.all())

@app.route("/teams/new/")
@login_required
def teams_form():
    return render_template("teams/new.html", form = TeamForm())

@app.route("/teams/add_point_<team_id>/", methods=["POST"])
@login_required
def teams_add_point(team_id):
    t = Team.query.get(team_id)

    t.points = t.points + 1
    db.session().commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/subtract_point_<team_id>/", methods=["POST"])
@login_required
def teams_subtract_point(team_id):
    t = Team.query.get(team_id)
    
    t.points = t.points - 1
    db.session().commit()

    return redirect(url_for("teams_index"))


@app.route("/teams/", methods=["POST"])
@login_required
def teams_create():
    form = TeamForm(request.form)
    
    if not form.validate():
        return render_template("teams/new.html", form=form)

    t = Team(name=form.name.data)
    t.race = form.race.data
    t.resurrect = form.resurrect.data
    t.account_id = current_user.id
    

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/delete_<team_id>", methods=["POST"])
@login_required
def teams_delete(team_id):
    t = Team.query.get(team_id)

    db.session.delete(t)
    db.session.commit()

    return redirect(url_for("teams_index"))