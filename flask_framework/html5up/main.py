from flask import Flask, render_template,abort

app = Flask(__name__,template_folder=r"C:\Users\PC\Desktop\Programming\python_projects\100daysofpython\flask_framework/html5up/templates")

@app.route("/")
def home():

    return render_template("site.html")

if __name__ == "__main__":
    app.run(debug=True)