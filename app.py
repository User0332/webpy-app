from secrets import token_urlsafe
from flask_session import Session
from flask import Flask

app = Flask(__name__, template_folder="html")

app.debug = True
app.secret_key = token_urlsafe(20)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False

Session(app)