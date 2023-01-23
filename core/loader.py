import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from deta import App

app = App(Flask(__name__))

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'].replace('postgres', 'postgresql+psycopg2')
app.config['SQLALCHEMY_POOL_SIZE'] = 3
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 