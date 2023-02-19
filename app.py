# -*- coding: utf-8 -*-
from flask_shop.setup import app,api
from flask_shop.model.Controler_Product import Controler_Product
from flask_shop.model.db import db


api.add_resource(Controler_Product, '/api/product')
@app.route('/')
def index():
    return '''
    <form action="/api/product" method="post" class="form-contact">
<p><label>title: </label> <input type="text" name="title" value="" requied />
<p><label>description: </label> <input type="text" name="description" value="" requied />
<p><label>type: </label> <input type="text" name="type" value="" requied />

<p><input type="submit" value="test" />
</form>
    '''
if __name__ == "__main__":
    app.run(debug=True)
