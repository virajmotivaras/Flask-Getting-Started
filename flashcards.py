from flask import Flask, render_template, abort
from model import db

app = Flask(__name__)

visitor_count = 0

@app.route("/")
def welcome():
    return render_template("welcome.html",
                           message="This is a message from the view")

@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html",
                               card=card,
                               index=index,
                               max_index=len(db) - 1)
    except IndexError:
        abort(404)


