from app import db


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    unit_price = db.Column(db.Float(2), nullable=False)
    multiplier = db.Column(db.Integer)
    sell_orders = db.relationship('SellOrder', backref='product', lazy=True)

    def __init__(self, name, unit_price, multiplier, id=None):
        self.id = id
        self.name = name
        self.unit_price = unit_price
        self.multiplier = multiplier
