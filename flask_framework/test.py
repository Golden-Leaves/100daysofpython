from flask import Flask

app = Flask(__name__)
def make_bold(func):
    def wrapper():
        text = func()

        return f"<b>{text}</b>"
    return wrapper
def make_emphasized(func):
    def wrapper():
        text = func()

        return f"<em>{text}</em>"
    return wrapper
def make_underlined(func):
    def wrapper():
        text = func()


        return f"<u>{text}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "Hi!"
@app.route("/<string:name>")
def stupidlol(name):
    return rf"""<h1 style='text-align: center'>Ngu nhu {name}</h1>
<p style='background-color: #FF123A'>Amogus</p>
<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3JqaG90OHR6c3hjeTNtOXczNmo0YnN1NGg4ZXFpNTBkMjJrbXZtYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TnUJHKyjwHXOM/giphy.gif" width = 200>
"""

@app.route("/text")
@make_bold
@make_emphasized
@make_underlined
def text():
    return "Bye"



if __name__ == "__main__":
    app.run(debug=True)
    