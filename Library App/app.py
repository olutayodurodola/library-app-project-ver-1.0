from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#import sqlite3
app = Flask(__name__)

app.secret_key = "myprecious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

db = SQLAlchemy(app)

import models
import views

db.create_all()