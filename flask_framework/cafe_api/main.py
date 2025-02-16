from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice
import os
from dotenv import load_dotenv
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
current_directory = os.path.dirname(os.path.abspath(__file__))
env_path  = os.path.join(current_directory,".env")
loaded = load_dotenv(env_path)
secret_api_key = os.getenv("API_KEY")
print(secret_api_key)
app = Flask(__name__)
DATABASE_NAME = "cafes"
# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
import os

db_path = os.path.abspath(f"./instance/{DATABASE_NAME}.db")

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):#Avoid the process of painstakingly creating dicts for jsonify()
        return {column.name:getattr(self,column.name,"Attribute Not Found") for column in self.__table__.columns}#Self is the instance itself e.g something.to_dict()

if not os.path.exists(rf"./instance/{DATABASE_NAME}.db"):
    with app.app_context():
        db.create_all()



@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    print(all_cafes)
    random_cafe = choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def location():
    location = request.args.get("loc")
    selected_cafe = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalar()
    if selected_cafe == None:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    else:
        return jsonify(cafe=selected_cafe.to_dict())
    
# HTTP POST - Create Record
@app.route("/add",methods=["POST"])
def add():
    if request.method == "POST":
        new_cafe = Cafe(
        name=request.form.get("name"),  # Get 'name' from form data
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),  
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success":"Successfully added new cafe.",})
# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id>",methods=["PATCH"])
def update_price(id):
    selected_cafe = db.session.get(Cafe,id)
    print(selected_cafe)
    if selected_cafe == None:
        return jsonify(error={"Not Found":'Sorry, a cafe with that id was not found in the database.'})
    else:
        new_price = request.args.get("new_price")
        selected_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success":'Successfully changed coffee price!'})
# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>",methods=["DELETE"])
def report_closed(id):
    api_key = request.args.get("api-key")
    print(api_key)
    if api_key == secret_api_key:
        cafe_to_delete = db.session.get(Cafe,id)
        if cafe_to_delete == None:
            return jsonify(error={"Not Found":'Sorry, a cafe with that id was not found in the database.'})
        else:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success":'Successfully deleted requested cafe!'})
    else:
        return jsonify(error={"Unauthorized":'Sorry, the API key you entered was incorrect.'})
        
        

if __name__ == '__main__':
    app.run(debug=True)
