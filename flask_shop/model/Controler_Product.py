

from flask_restful import Resource
from gridfs import GridFS

from flask_shop.model.db import db, mongo
from .Products import Product, Type

from flask import request

class Controler_Product(Resource):
    def get(self):
        info = Product.query.all()
        data = {}
        storage = GridFS(mongo.db, 'fs')
        for i in info:
            s = str(i.id) + " name " + str(i.title)
            d = str(i.description)
            t = str(i.type)
            image = str(i.image_name)
            fileobj = storage.get_version(filename=image, version=-1)

            data[i.id] = (s,d,t,str(fileobj.read()))


        return { "data": data }
    def post(self):
        try:
            n = request.form['image_name']
            f = request.files['file']
            mongo.save_file(filename=n, fileobj=f)
            t = Type(name=request.form['type'])
            db.session.add(t)
            db.session.flush()
            p = Product(title=request.form['title'], description=request.form['description'], type=request.form['type'],image_name=request.form['image_name'])
            db.session.add(p)
            db.session.flush()
            db.session.commit()
            return {"result": "ok"}
        except Exception as e:
            db.session.rollback()
            return {"result": e.__str__(),
                    "title" : request.form['title'],
                    "description" : request.form['description'],
                    "type" :request.form['type'],
                    }




