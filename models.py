#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import environ
from sqlalchemy import Column, String, Integer, DateTime, \
    create_engine, ForeignKey, Date
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate


# from your environment variables
#ex: export database_path=YOUR_DATABASE_PATH
datebase_path = environ.get('datebase_path')

db = SQLAlchemy()
migrate = Migrate()


def setup_db(app, datebase_path=datebase_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = datebase_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)


    

class Movie(db.Model):

    __tablename = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    release_date = Column(Date)
    image_url = Column(String)
    stuff = db.relationship('Actor', backref='show')

    def __init__(
        self,
        title,
        release_date,
        image_url,
        ):
        self.title = title
        self.release_date = release_date
        self.image_url = image_url

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'image_url': self.image_url,
            }


class Actor(db.Model):

    __tablename = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(Integer)
    gender = Column(String)
    image_url = Column(String)
    movie_id = Column(Integer, ForeignKey('movie.id'), nullable=True)

    def __init__(
        self,
        name,
        age,
        gender,
        movie_id,
        image_url
        ):
        self.name = name
        self.age = age
        self.gender = gender
        self.movie_id = movie_id
        self.image_url = image_url

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movie_id': self.movie_id,
            'image_url': self.image_url,
            }
