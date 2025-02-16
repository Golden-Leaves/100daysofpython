from flask import Flask, render_template,abort
import requests

app = Flask(__name__)

@app.route("/guess/<string:name>")
def guess(name):
    name = name.title()
    agify_parameters = {
        "name": name,
    }
    agify_response = requests.get("https://api.agify.io",params=agify_parameters)
    agify_data = agify_response.json()
    
    print(f"You have {agify_response.headers["x-rate-limit-remaining"]} times left for agify.")
    genderize_parameters = {
        "name": name,
    }
    genderize_response = requests.get("https://api.genderize.io",params=genderize_parameters)
    print(f"You have {genderize_response.headers["x-rate-limit-remaining"]} times left for genderize.")
    genderize_data = genderize_response.json()
    
    return f"""<h1>Hey {name},</h1>
<h2>I think you are {genderize_data["gender"]}</h2>
<h3>And maybe {agify_data["age"]} years old</h3>
<h2 style="text-align:center">You have {genderize_response.headers["x-rate-limit-remaining"]} tries left.</h2>
"""
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/blog/<int:num>")
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("fake_blog.html",posts=all_posts)
if __name__ == "__main__":
    app.run(debug=True)