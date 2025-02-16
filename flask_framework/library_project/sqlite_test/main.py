import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True,nullable=False)
    title: Mapped[str] = mapped_column(String(250),unique=True,nullable=False)
    author: Mapped[str] = mapped_column(String(250),nullable=False)
    rating: Mapped[int]= mapped_column(Float,nullable=False)

# with app.app_context():
#     book = Books(title="Harry Potter",author="J.K Rowling",rating=9.3)
#     db.session.add(book)
#     db.session.commit()

with app.app_context():
    book_to_delete = db.session.execute(db.select(Books).where(Books.title == "Harry Potter and the Chamber of Secrets")).scalar()
    db.session.delete(book_to_delete)
     # or book_to_update = db.get_or_404(Book, book_id)  
    db.session.commit()
print("Done")


