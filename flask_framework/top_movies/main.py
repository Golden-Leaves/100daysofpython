from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float,Date
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,FloatField
from wtforms.validators import DataRequired,InputRequired,Email,Length,NumberRange
import requests
import os
from dotenv import load_dotenv,find_dotenv
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_MOVIE_URL = "https://api.themoviedb.org/3/movie/" #URLS for different search types(id,name,...)
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/original/"
# current_directory = os.path.dirname(os.path.abspath(__file__))
# env_path = os.path.join(current_directory, ".env")  
loaded = load_dotenv(r"C:\Users\PC\Desktop\Programming\python_projects\100daysofpython\flask_framework\top_movies\.env")
access_token = os.getenv("ACCESS_TOKEN")
print(loaded)
print(access_token)

class Base(DeclarativeBase):
    pass

DATABASE_NAME = "top_movies_collection"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(500), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    
if not os.path.isfile(f"./instance/{DATABASE_NAME}.db"):
    with app.app_context():
        db.create_all()

        
class RateMovieForm(FlaskForm):
    rating = FloatField("Your rating out of 10",validators=[InputRequired(message="Empty Field"),NumberRange(message="Rating exceeded 10",max=10)])
    review = StringField("Your Review",validators=[InputRequired(message="Empty Field"),Length(max=250,message="Review too long (max:250 words)")])
    submit = SubmitField("Done")
    
class AddMovieForm(FlaskForm):
    title = StringField("Movie Title",validators=[InputRequired("Empty Field"),Length(max=250,message="Review too long (max:250 words)")])
    submit = SubmitField("Done")
    
@app.route("/")
def home():
   
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
        db.session.commit()
        
    return render_template("index.html",movies=movies,tmdb_image_url=TMDB_IMAGE_URL)

@app.route("/edit",methods=["GET","POST"])
def edit():
    rating_movie_form = RateMovieForm()
    if rating_movie_form.validate_on_submit():
        id = request.args.get("id")
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        movie_to_update.rating  = rating_movie_form.rating.data
        movie_to_update.review = rating_movie_form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    movie_id = request.args.get("id")
    return render_template("edit.html",id=movie_id,form=rating_movie_form)



@app.route("/delete")
def delete():
    id = int(request.args.get("id"))
    book_to_delete = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add",methods=["GET",'POST'])
def add():
    
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        movie_title = add_form.title.data
        parameters = {
            "query": movie_title,
        }
        head = {
            "Authorization": f"Bearer {access_token}"  
        }
        response = requests.get(url=TMDB_SEARCH_URL,params=parameters,headers=head)
        print(response.text)
        data = (response.json())["results"]
#         movie_to_add = Movie(title=data["title"],
#                              year=int(data["release_date"].split("-")[0]),
#                              description=data["overview"],
#                              rating=data["vote_average"],
#                              ranking=data[""]

# )
        return render_template("select.html",results=data)
    return render_template("add.html",form=add_form)
@app.route("/find")
def find():
    
    id = request.args.get("id")
    parameters = {
            "external_source": id,
        }
    head = {
        "Authorization": f"Bearer {access_token}"  
    }
    response = requests.get(url=TMDB_MOVIE_URL + id,params=parameters,headers=head)
    print(response.text)
    data = response.json()
    movie_to_add = Movie(title=data["title"],
                         year=data["release_date"].split("-")[0],
                         description=data["overview"],
                         img_url=data["poster_path"],
                         )
    db.session.add(movie_to_add)
    db.session.commit()
    ranking_id = db.session.execute(db.select(Movie).where(Movie.title == data["title"])).scalar()
    return redirect(url_for("edit",id=ranking_id.id))

if __name__ == '__main__':
    app.run(debug=True)
