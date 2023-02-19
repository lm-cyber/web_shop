

from flask_restful import Resource
from flask_shop.model.db import db
from .Products import Product
from flask import request

class Controler_Product(Resource):
    def get(self):
        info = Product.query.all()
        data = {}
        for i in info:
            s = str(i.id) + " name " + str(i.title)
            d = str(i.description)
            t = str(i.type)
            data[i.id] = (s,d,t)

        return { "data": data }
    def post(self):
        try:
            p = Product(title=request.form['title'], description=request.form['description'], type=request.form['type'])
            db.session.add(p)
            db.session.flush()
            db.session.commit()
            return {"result": "ok"}
        except :
            db.session.rollback()
            return {"result": "problem",
                    "title" : request.form['title'],
                    "description" : request.form['description'],
                    "type" :request.form['type'],
                    }



