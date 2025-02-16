from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,URLField,TimeField,SelectField
from wtforms.validators import InputRequired,Email,Length,URL
import csv


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[InputRequired(message="Empty Field")])
    location_url = URLField(label="Location URL",validators=[InputRequired(message="Empty Field"),URL(message="Invalid URL")])
    open_time = TimeField(label="Opening Time",validators=[InputRequired(message="Empty Field")])
    closing_time = TimeField(label="Closing Time",validators=[InputRequired(message="Empty Field")])
    coffee_rating = SelectField(label="Coffee Rating",choices=["☕","☕" * 2,"☕" * 3,"☕" * 4,"☕" * 5])
    wifi_strength_rating = SelectField(label="Wifi Strength Rating",choices=["💪","💪"*2,"💪"*3,"💪"*4,"💪"*5])
    power_outlet_rating = SelectField(label="Power Outlet Rating",choices=["🔌","🔌"*2,"🔌"*3,"🔌"*4,"🔌"*5])
    
       
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        cafe_name = form.cafe.data
        location_url = form.location_url.data
        opening_time = form.open_time.data.strftime("%H/%M")
        closing_time = form.closing_time.data.strftime("%H/%M")
        coffee_rating = form.coffee_rating.data
        wifi_strength_rating = form.wifi_strength_rating.data
        power_outlet_rating = form.power_outlet_rating.data
        with open('./flask_framework/coffee_and_wifi/cafe-data.csv',"a", newline='', encoding='utf-8') as csv_file:
            csv_file.write("\n"+(",".join([cafe_name,location_url,opening_time,closing_time,coffee_rating,wifi_strength_rating,power_outlet_rating])))
            
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('./flask_framework/coffee_and_wifi/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
