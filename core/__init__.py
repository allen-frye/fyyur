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



# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY=os.urandom(32),
#         DEBUG = True,
#         # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:plumbflo22!@localhost:5432/fyyur'

#     )
#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page that says hello
#     @app.route('/hello')
#     def hello():
#         return 'Hello, World!'

#     return app