from flask import Flask, render_template,abort,request
import requests

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login", methods=["POST"])
def login():
    password = request.form["password"]
    username= request.form["username"]
    return rf"""<h1>{username}</h1>
<h1>{password}</h1>"""
if __name__ == "__main__":
    app.run(debug=True)