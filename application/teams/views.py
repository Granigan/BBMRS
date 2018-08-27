from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.teams.models import Team
from application.teams.forms import TeamForm
from application.contestteam.models import ContestTeam
from application.matches.models import Match

@app.route("/teams", methods=["GET"])
def teams_index():
    return render_template("teams/list.html", teams = Team.find_teams_and_coaches())

@app.route("/teams/new/")
@login_required()
def teams_form():
    return render_template("teams/new.html", form = TeamForm())

#@app.route("/teams/add_point_<team_id>/", methods=["POST"])
#@login_required
#def teams_add_point(team_id):
#    t = Team.query.get(team_id)
#
#    t.points = t.points + 1
#    db.session().commit()
#
#    return redirect(url_for("teams_index"))

#@app.route("/teams/subtract_point_<team_id>/", methods=["POST"])
#@login_required
#def teams_subtract_point(team_id):
#    t = Team.query.get(team_id)
#    
#    t.points = t.points - 1
#    db.session().commit()
#
#    return redirect(url_for("teams_index"))


@app.route("/teams/", methods=["POST"])
@login_required()
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
@login_required(role="ADMIN")
def teams_delete(team_id):

    for id in ContestTeam.find_contests_by_team(team_id):
        ct = ContestTeam.query.get(id)
        db.session.delete(ct)
    db.session.commit()

    t = Team.query.get(team_id)

    db.session.delete(t)
    db.session.commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/details_<team_id>", methods=['GET'])
def team_details(team_id):
    t = Team.query.get(team_id)

    return render_template("teams/details.html", team = t,
        matches = Match.find_match_history(team_id),
        total = Match.find_total_games_played_by_team(team_id),
        wins = Match.find_wins_by_team(team_id),
        losses = Match.find_losses_by_team(team_id),
        percentage = Match.find_win_percentage_by_team(team_id)
        )
