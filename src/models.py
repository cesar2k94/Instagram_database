import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'),
        nullable=False)
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    firstname = Column(String(10), nullable=False)
    lastname = Column(String(10), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    follower = relationship('Follower')
    post = relationship('Post')
    comment = relationship('Comment')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    comment = relationship('Comment')   
    media = relationship('Media')   

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(30), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'),
        nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')