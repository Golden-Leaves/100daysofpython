from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


DATABASE_NAME = "books_collection"
class Base(DeclarativeBase):
    pass
all_books = []
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(250),unique=True,nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float,nullable=False)
    
if not os.path.isfile(f"./instance/{DATABASE_NAME}.db"):
    with app.app_context():
        db.create_all()
#Retrieve all book data
@app.route("/")
def home():
    all_books = db.session.execute(db.select(Books).order_by(Books.title)).scalars().all()
    print([book.title for book in all_books])
    return render_template("index.html",books=all_books)


@app.route("/add",methods=["GET","POST"])
def add():
    if request.method == "POST":
        book_name = request.form["book_name"]
        book_author = request.form["book_author"]
        book_rating = request.form["book_rating"]
        book_dictionary = {
            "title": book_name,
            "author":book_author,
            "rating":book_rating,
            
        }
        with app.app_context():
            print("yes")
            book = Books(title=book_dictionary["title"],author=book_dictionary["author"],rating=book_dictionary["rating"])
            db.session.add(book)
            db.session.commit()
        
        print(all_books)
        return redirect(url_for("home"))
  
    return render_template("add.html")
@app.route("/edit",methods=["GET","POST"])
def edit():
    if request.method == "POST":
        with app.app_context():
            book_id = request.args.get("id") 
            book_to_update = db.get_or_404(Books,book_id)
            book_to_update.rating = request.form["new_rating"]
            db.session.commit()
            print("Sucessfully updated new rating.")
            return redirect(url_for("home"))
            
        

    book_id = request.args.get("id") 
    selected_book = db.get_or_404(Books,book_id)
    return render_template("edit.html",book=selected_book)
@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book_to_delete = db.get_or_404(Books,book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))
    


if __name__ == "__main__":
    app.run(debug=True)

