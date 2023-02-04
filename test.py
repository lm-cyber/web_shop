from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@localhost/docker'
db =SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=True)
    name = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f"<users {self.id, self.name}"


@app.route("/")
def test():
    return render_template("index.html")

@app.route("/image/")
def image():
	return render_template("image.html")



if __name__ == "__main__":
    app.run(debug=True)
