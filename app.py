# -*- coding: utf-8 -*-
from flask_shop.setup import app,api
from flask_shop.model.test_resource import Users_
api.add_resource(Users_, '/')

if __name__ == "__main__":
    app.run(debug=True)
