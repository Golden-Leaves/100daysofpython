from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship,DeclarativeBase
from sqlalchemy import ForeignKey
from flask_login import UserMixin
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
# or: db = SQLAlchemy(app, model_class=Base) if you're using declarative Base manually
db.init_app(app)
class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)

    # One user -> many posts
    posts = relationship('Post', back_populates='author', cascade="all, delete")

class Post(db.Model):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[str] = mapped_column(nullable=False, unique=True)
    subtitle: Mapped[str] = mapped_column(nullable=True)
    image_url: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    author = relationship('User', back_populates='posts')

with app.app_context():
    db.create_all()
    print('Tables created successfully.')
