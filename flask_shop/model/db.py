from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
import gridfs
from pymongo import MongoClient

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://admin:admin@localhost:27017/test123?authSource=admin'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@localhost:5432/docker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "e17e3020a113b16c340059e2d437703e4eea00a707c3aa2ac93e0fc23869"
db = SQLAlchemy(app)
mongo = PyMongo(app)

fs = gridfs.GridFS(mongo.db)