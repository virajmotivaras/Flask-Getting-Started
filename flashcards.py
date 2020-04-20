from flask import Flask

app = Flask(__name__)

visitor_count = 0

@app.route("/")
def welcome():
    return "Welcome to flash cards application"

@app.route("/viewed")
def visitors_count():
    global visitor_count
    visitor_count += 1
    return "This pae has been viewed {count} number of times".format(count=visitor_count)

