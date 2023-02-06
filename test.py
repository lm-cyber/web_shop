from sqlalchemy.sql import expression
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@localhost/docker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db =SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=True)
    name = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f"<users {self.id, self.name}"



@app.route("/")
def index():
    info = []
    try:
        info = Users.query.all()
        print(info)
    except:
        print("Ошибка чтения из БД")

    return render_template("index.html", title="Главная", list=info)


@app.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":
        try:
            hash = generate_password_hash(request.form['psw'])
            u = Users(email=request.form['email'], password=hash, name=request.form['name'])
            db.session.add(u)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")

        return redirect(url_for('index'))

    return render_template("register.html", title="Регистрация")



@app.route("/db/")
def db_():
    try:
        db.create_all()
        db.session.flush()
        return "ок"
    except:
        return "bad "













# @app.route("/create/")
# def create():
#     db.create_all()
#     return 'ok'
#
#
# @app.route("/")
# def test():
#     return render_template("index.html")
#
# @app.route("/image/")
# def image():
# 	return render_template("image.html")



if __name__ == "__main__":
    app.run(debug=True)
