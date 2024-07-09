from app import app
from flask import render_template


@app.route("/")
@app.route("/home")
def home():
    return render_template("home/home.html")


@app.route("/goals")
def goals():
    return render_template("home/goals.html")

@app.route("/website")
def website():
    return render_template("home/website.html")