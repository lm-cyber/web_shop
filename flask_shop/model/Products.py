from flask_shop.model.db import db






class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    price = db.Column(db.DECIMAL(10, 2))
    description = db.Column(db.Text())

    def __str__(self):
        return self.title

    def __iter__(self):
        return iter(self.variants)
    
    def __repr__(self):
        return f"<users {self.id, self.name}"


   
    
