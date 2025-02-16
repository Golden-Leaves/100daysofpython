from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL,InputRequired
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class FormClass(FlaskForm):
        title = StringField(label="Blog Post Title",validators=[InputRequired("Empty Field")])
        subtitle = StringField(label="Subtitle",validators=[InputRequired("Empty Field")])
        name = StringField(label="Your Name",validators=[InputRequired("Empty Field")])
        img_url = StringField(label="Image URL",validators=[InputRequired("Empty Field"),URL()])
        blog_content = CKEditorField(label="Blog Content",validators=[InputRequired("Empty Field")])
        submit = SubmitField(label="Submit")
        
# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost,post_id)
    return render_template("post.html", post=requested_post)


# Add a new post
@app.route("/new-post",methods=["GET","POST"])
def new_post():
    
    Form = FormClass()
    if Form.validate_on_submit():
        title = Form.title.data
        subtitle = Form.subtitle.data
        name = Form.name.data
        img_url = Form.img_url.data
        blog_content = Form.blog_content.data
        submitted_data = BlogPost(title=title,
                                  subtitle=subtitle,
                                  author=name,
                                  img_url=img_url,
                                  body=blog_content,
                                  date=date.today().strftime("%B %#d, %Y"))
        db.session.add(submitted_data)
        db.session.commit()
        
    return render_template("make-post.html",form=Form,h1="New Post")
# Edit an existing post
@app.route("/edit-post/<int:post_id>",methods=["GET","POST"])
def edit_post(post_id):

    current_post = db.get_or_404(BlogPost,post_id)
    
    Form = FormClass(title=current_post.title,
                     subtitle=current_post.subtitle,
                     name=current_post.author,
                     img_url=current_post.img_url,
                     blog_content=current_post.body)
    
    if Form.validate_on_submit():
        title = Form.title.data
        subtitle = Form.subtitle.data
        name = Form.name.data
        img_url = Form.img_url.data
        blog_content = Form.blog_content.data
        #Update post in db
        current_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
        current_post.title = title
        current_post.subtitle = subtitle
        current_post.author = name
        current_post.img_url = img_url
        current_post.body = blog_content
        db.session.commit()
        
        
    return render_template("make-post.html",h1="Edit Post",form=Form)
# Deletes an existing post
@app.route("/delete/<int:post_id>")
def delete(post_id):
    post_to_be_deleted = db.get_or_404(BlogPost,post_id)
    db.session.delete(post_to_be_deleted)
    db.session.commit()
    return redirect(url_for("get_all_posts"))
# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
