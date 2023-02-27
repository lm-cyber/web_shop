# -*- coding: utf-8 -*-
import base64

from flask import make_response
from gridfs import GridFS

from flask_shop.setup import app,api
from flask_shop.model.Controler_Product import Controler_Product
from flask_shop.model.Controler_Image import Controler_Image
from flask_shop.model.db import db, mongo

api.add_resource(Controler_Product, '/api/product')
api.add_resource(Controler_Image, '/api/image')
@app.route('/')
def index():
    return '''
    <form action="/api/product" method="post" class="form-contact" enctype = "multipart/form-data">
<p><label>title: </label> <input type="text" name="title" value="" requied />
<p><label>description: </label> <input type="text" name="description" value="" requied />
<p><label>type: </label> <input type="text" name="type" value="" requied />
<p><label>image: </label> <input type="text" name="image_name" value="" requied />
         <input type = "file" name = "file" />

<p><input type="submit" value="test" />
</form>
<h1> aaaaaaaaaaaaaaaa   </h1>
   <form action = "/api/image" method = "POST"
         enctype = "multipart/form-data">
         <input type = "text" name = "name"/>
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
      <h1> aaaaaaaaaaaaaaaa   </h1>
        <form action = "/api/image" method = "PUT">
                 <input type = "submit"/>

        </form>
    '''

@app.route('/images/')
def get_image():
    try:
        storage = GridFS(mongo.db, 'fs')
        fileobj = storage.get_version(filename='12312', version=-1)
        response = make_response(fileobj.read())
        response.headers.set('Content-Type', 'image/jpeg')
        response.headers.set(
            'Content-Disposition', 'attachment', filename='fon.jpg')
        return response
    except Exception as e:
        return e.__str__();
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
