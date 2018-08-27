from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.matches.forms import MatchForm
from application.teams.models import Team
from application.matches.models import Match

@app.route("/match/new")
@login_required()
def match_form():
    form = MatchForm()
    form.find_teams(Team.query.all())
    return render_template("matches/new.html", form=form)

@app.route("/match", methods=["POST"])
@login_required()
def match_report():
    form = MatchForm(request.form)

    m = Match(winner_id=form.winner.data, loser_id=form.loser.data)
    
    db.session().add(m)
    db.session().commit()

    return redirect(url_for("contests_index"))
