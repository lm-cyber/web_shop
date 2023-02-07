from flask_shop.model.db import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=True)
    name = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<users {self.id, self.name}"