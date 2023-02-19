# -*- coding: utf-8 -*-
from flask_shop.setup import app,api
from flask_shop.model.Controler_Product import Controler_Product
api.add_resource(Controler_Product, '/api/product')
@app.route('/')
def index():
    return "tipo front"
if __name__ == "__main__":
    app.run(debug=True)
