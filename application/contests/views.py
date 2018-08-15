from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.contests.models import Contest
from application.contests.forms import ContestForm

@app.route("/contests", methods=["GET"])
def contests_index():
    return render_template("contests/list.html", contests = Contest.query.all())

@app.route("/contests/new/")
@login_required
def contest_form():
    return render_template("contests/new.html", form=ContestForm())

@app.route("/contests", methods=["POST"])
@login_required
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
@login_required
def contest_delete(contest_id):
    c = Contest.query.get(contest_id)

    db.session.delete(c)
    db.session.commit()

    return redirect(url_for("contests_index"))

@app.route("/contests/details_<contest_id>", methods=['GET'])
def contest_details(contest_id):
    # add validation for checking if contest exists
    c = Contest.query.get(contest_id)

    return render_template("contests/details.html", contest = c)
