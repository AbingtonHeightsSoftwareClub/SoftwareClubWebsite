from app import app
from flask import render_template

@app.errorhandler(404)
# Inbuilt function that takes in error
def not_found(e):
    return render_template("errors/404.html")