# -*- coding: utf-8 -*-
from flask_shop.setup import app,api
from flask_shop.model.Controler_Product import Controler_Product
from flask_shop.model.Controler_Image import Controler_Image
from flask_shop.model.db import db


api.add_resource(Controler_Product, '/api/product')
api.add_resource(Controler_Image, '/api/image')
@app.route('/')
def index():
    return '''
    <form action="/api/product" method="post" class="form-contact">
<p><label>title: </label> <input type="text" name="title" value="" requied />
<p><label>description: </label> <input type="text" name="description" value="" requied />
<p><label>type: </label> <input type="text" name="type" value="" requied />

<p><input type="submit" value="test" />
</form>
<h1> aaaaaaaaaaaaaaaa   </h1>
   <form action = "/api/image" method = "POST"
         enctype = "multipart/form-data">
         <input type = "text" name = "name"/>
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
    '''
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
