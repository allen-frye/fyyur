import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
#did not add basedir to mapped config
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

 
# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:plumbflo22!@localhost:5432/fyyu'r
