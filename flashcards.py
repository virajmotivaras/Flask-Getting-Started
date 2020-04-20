from flask import Flask, render_template

app = Flask(__name__)

visitor_count = 0

@app.route("/")
def welcome():
    return render_template("welcome.html",
                           message="This is a message from the view")

