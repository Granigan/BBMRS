from application import app
from flask import render_template, request

@app.route("/teams/new/")
def teams_form():
    return render_template("teams/new.html")

@app.route("/teams/", methods=["POST"])
def teams_create():
    print(request.form.get("name"))

    return "hello again, world"