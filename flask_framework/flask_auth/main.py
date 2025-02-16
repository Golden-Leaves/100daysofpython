from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory,abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
from dotenv import load_dotenv
current_directory = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_directory,".env")
yes = load_dotenv(env_path)


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret-key")
print(os.getenv("SECRET_KEY", "fallback-secret-key"))
# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
# CREATE TABLE IN DB


class User(db.Model,UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        if db.session.execute(db.select(User).where(User.email == email)).scalar() != None:
            flash("Email already exists, please login.")
            return redirect(url_for("login"))
        name = request.form["name"]
        password = generate_password_hash(request.form["password"],method="pbkdf2",salt_length=8)
        user = User(email=email,password=password,name=name)
        db.session.add(user)
        db.session.commit()
        print(user.id)
        #SQLAlchemy automatially assigns id to instance after committing
        logged_in = login_user(user)
        print(logged_in)
        return render_template("secrets.html",name=name)
    return render_template("register.html")


@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":

        email = request.form["email"]
        user_info = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user_info == None:
            flash("Your email does not exist.")
            return redirect(url_for("login"))
        password = check_password_hash(pwhash=user_info.password,password=request.form["password"])
        print(password)
        #Correct password or nah
        if password:
            login_user(user_info)
            return redirect(url_for("secrets"))
        else:
            print("no")
            flash("Incorrect Password.")
        
            
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    pass

@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()


if __name__ == "__main__":
    app.run(debug=True)
