

from flask_restful import Resource

from .Products import Product

class Product_(Resource):
    def get(self):
        info = Product.query.all()
        data = {}
        for i in info:
            s = str(i.id) + " name " + str(i.title)
            d = str(i.description)
            data[i.id] = (s,d)

        return { "data": data }
    def post(self):
        pass

