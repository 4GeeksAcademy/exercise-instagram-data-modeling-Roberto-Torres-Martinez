import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column
from sqlalchemy import create_engine
from eralchemy2 import render_er
from typing import Literal

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    follower = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    get_id1 = Column(Integer, ForeignKey('post.id'))
    get_id2 = Column(Integer, ForeignKey('comment.id'))
    follower = relationship('follower', backref= 'user')
    comment = relationship('comment', backref= 'user')
    post = relationship('follower', backref= 'user')

FyleType = Literal['PHOTO', 'VIDEO', 'AUDIO']


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type: Mapped[FyleType] = mapped_column(String, nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    media = relationship('media', backref= 'post')
    comment = relationship('comment', backref= 'post')

class Comment(Base):
     __tablename__ = 'comment'
     id = Column(Integer, primary_key=True)
     comment_text = Column(String(250), nullable=False)
     post_id = Column(Integer, ForeignKey('post.id'))
# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e