from flask_restful import Resource
from gridfs import GridFS

from flask_shop.model.db import fs,mongo
from flask import request
from bson.objectid import ObjectId
class Controler_Image(Resource):
    def get(self):
        try:
            n = request.args.get("name")
            storage = GridFS(mongo.db, 'fs')
            fileobj = storage.get_version(filename=n, version=-1)
            return {"result" : str(fileobj.read())}
        except Exception as e:
            return {"result": e.__str__()}
    def post(self):
        try:
            n = request.form['name']
            f = request.files['file']
            mongo.save_file(filename=n,fileobj=f)
            return {"result" : "done"}
        except Exception as e:
            return {"result":e.__str__()}

    def put(self):
        files = [fs.get_last_version(file) for file in fs.list()]
        s=''
        for i in files:
            s+= str(i._id)
        return {"data" :str(s) }