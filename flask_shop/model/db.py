from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@localhost/docker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "e17e3020a113b16c340059e2d437703e4eea00a707c3aa2ac93e0fc23869"
db = SQLAlchemy(app)
