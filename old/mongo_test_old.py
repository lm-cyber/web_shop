from flask import Flask, request, url_for
from flask_pymongo import PyMongo

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://admin:admin@localhost:27017/test'
mongo = PyMongo(app)




@app.route('/')
def index():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post action="/create" enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''




@app.route('/create', methods=['POST'])
def create():
    profile_image = request.files['file']
    mongo.save_file(profile_image.filename, profile_image)
    mongo.db.users.insert({'username' : request.form.get('username'), 'profile_image_name' : profile_image.filename })
    return "done"

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


if __name__ == "__main__":
    app.run(debug=True)
