from flask_shop.model.db import db




class Type(db.Model):
    __tablename__ = 'type'
    name = db.Column(db.String(100), primary_key=True)


    def __str__(self):
        return self.name


    def __iter__(self):
        return iter(self.name)


    def __repr__(self):
        return f" {self.name}"


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text())
    type = db.Column(db.String(100), db.ForeignKey("type.name"))


    def __str__(self):
        return self.title

    def __iter__(self):
        return iter(self.id)
    
    def __repr__(self):
        return f" {self.id, self.title}"



   
    
