from flask import Flask, render_template
import requests
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,InputRequired,Email,Length
from flask_bootstrap import Bootstrap5



'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class FormClass(FlaskForm):
        email = StringField(label='Email', validators=[InputRequired(message="Empty Field"),Email(message="Invalid email address")])
        password = PasswordField(label='Password', validators=[InputRequired(message="Empty Field"),Length(min=8,message="Password needs to be at least 8 characters")])
        submit = SubmitField(label="Log In")

app = Flask(__name__)
secret_email = "admin@email.com"
secret_password = "12345678"
app.secret_key = "Golden_Leaves"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    WTForms = FormClass()
    if WTForms.validate_on_submit():
        if WTForms.email.data == secret_email and WTForms.password.data == secret_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html",form=WTForms)

if __name__ == '__main__':
    app.run(debug=True)
