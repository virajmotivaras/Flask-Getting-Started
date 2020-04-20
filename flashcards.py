from flask import Flask, render_template
from model import db

app = Flask(__name__)

visitor_count = 0

@app.route("/")
def welcome():
    return render_template("welcome.html",
                           message="This is a message from the view")

@app.route("/card")
def card():
    card = db[0]
    return render_template("card.html", card=card)

