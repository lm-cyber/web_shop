from flask_restful import Resource
from flask_shop.model.db import fs
from flask import request
from bson.objectid import ObjectId
class Controler_Image(Resource):
    def get(self):
        try:
            n = request.args.get("name")
            return fs.get(ObjectId(n)).read()
        except Exception as e:
            return {"result": e.__str__()}
    def post(self):
        try:
            n = request.form['name']
            f = request.files['file']
            id = fs.put(f, content_type=f.content_type, filename=n)
            return {"result" : str(id)}
        except Exception as e:
            return {"result":e.__str__()}

    def put(self):
        files = [fs.get_last_version(file) for file in fs.list()]
        return {"data" :str(files) }