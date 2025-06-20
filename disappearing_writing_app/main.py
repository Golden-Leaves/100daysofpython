from datetime import datetime
from flask import Flask, abort, render_template, redirect, url_for, flash,session
from flask_session import Session
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text,ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# from forms import CreatePostForm,RegisterForm,LoginForm,CommentForm
import os
from dotenv import load_dotenv
from prompts import prompt_list


current_directory = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_directory,".env")
print(env_path)
load_dotenv(env_path)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config["SESSION_TYPE"] = "filesystem"
ckeditor = CKEditor(app)
Session(app)
Bootstrap5(app)



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def user_loader(user_id):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

with app.app_context():
    db.create_all()

#Decorator to check for admin status
def admin_only(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if current_user.id != 1:
            abort(403)
        else:
            return func(*args,**kwargs)
    return wrapper


class User(db.Model,UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    
@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/random-prompt-generator")
def generate_prompt():
   return render_template("generate_prompt.html")

@app.route("/write")
def write():
   return render_template("write.html")

if __name__ == "__main__":
    app.run(debug=True) 
