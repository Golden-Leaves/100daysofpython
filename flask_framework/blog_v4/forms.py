from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import InputRequired, URL,Email,Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[InputRequired(message="Empty Field")])
    subtitle = StringField("Subtitle", validators=[InputRequired(message="Empty Field")])
    img_url = StringField("Blog Image URL", validators=[InputRequired(message="Empty Field"), URL()])
    body = CKEditorField("Blog Content", validators=[InputRequired(message="Empty Field")])
    submit = SubmitField("Submit Post")



class RegisterForm(FlaskForm):
    name = StringField("Username",validators=[InputRequired(message="Empty Field")])
    email = StringField("Email",validators=[InputRequired(message="Empty Field"),Email(message="Enter a valid email address")])
    password = PasswordField("Password",validators=[InputRequired(message="Empty Field")])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email",validators=[InputRequired(message="Empty Field"),Email(message="Enter a valid email address")])
    password = PasswordField("Password",validators=[InputRequired(message="Empty Field")])
    submit = SubmitField("Login")


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    body = CKEditorField("Comment",validators=[Length(max=500,min=1,message="Comment exceeded length limit or is empty.")])
    submit = SubmitField("Submit")
    