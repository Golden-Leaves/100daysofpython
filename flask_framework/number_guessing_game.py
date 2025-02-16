from flask import Flask
import random
random_number = random.randint(1,10)
def make_bold(func):
    def wrapper():
        text = func()
        return f"<b>{text}</b>"
        
    return wrapper
app = Flask(__name__)
@app.route("/")
@make_bold
def welcome():
    return """<h1>Welcome to the number guessing game!</h1>
<p>Guess the number by adding "/{number}"(1-10) to the end of the url!
"""
@app.route("/<int:number>")
def number_page(number):
    if number < random_number:
        return f"""<h1 style="color: #FF0000">{number} is lower than the correct number!</h1>
<img src="https://media3.giphy.com/media/3hv1Ux7SRfzd6VTBSL/giphy.webp?cid=790b761196bdazsd20dh2r0bk79wyzpbqho757mj4cvr47i2&ep=v1_gifs_search&rid=giphy.webp&ct=g">
    """
    elif number > random_number:
        return f"""<h1 style="color: #FF0000">{number} is higher than the correct number!</h1>
    <img src="https://media3.giphy.com/media/3hv1Ux7SRfzd6VTBSL/giphy.webp?cid=790b761196bdazsd20dh2r0bk79wyzpbqho757mj4cvr47i2&ep=v1_gifs_search&rid=giphy.webp&ct=g">
    """
    else:
        return  f"""<h1 style="color: #00FF00">{number} is the correct number!</h1>
    <img src="https://media2.giphy.com/media/8ta93xRKDxucy8zfNp/200.webp?cid=790b76114q7i0894fh4lvrn4p7pir9rgk0023imei0z5ej9m&ep=v1_gifs_search&rid=200.webp&ct=g">
    """
    
if __name__ == "__main__":
    app.run(debug=True)
    