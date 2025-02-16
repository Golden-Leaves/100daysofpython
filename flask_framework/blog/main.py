from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()
post_objs = []
for post in all_posts:
    post_obj = Post(post["title"],post["subtitle"],post["body"],post["id"])
    post_objs.append(post_obj)
@app.route('/')
def home():
    global post_objs
    return render_template("index.html",posts=all_posts)
@app.route("/post/<int:id>")
def post(id):
    global post_objs
    return render_template("post_site.html",posts=post_objs,required_id = id)
if __name__ == "__main__":
    
    app.run(debug=True)
