from flask import Flask
import os
import logging
from logging import Formatter, FileHandler

basedir = os.path.abspath(os.path.dirname(__file__))
# basedir = os.getcwd()

app = Flask(__name__)

#config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/dev.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:plumbflo22!@localhost:5432/fyyur'
app.config['SECRET_KEY'] = os.urandom(32)
app.config['DEBUG'] = True

import views

# For separation of concerns, I followed the approach in this article: https://dev.to/curiouspaul1/creating-modularized-flask-apps-with-blueprints-19nc