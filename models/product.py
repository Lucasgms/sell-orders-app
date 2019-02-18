from flask import jsonify
from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    unit_price = db.Column(db.Float(2), nullable=False)
    multiplier = db.Column(db.Integer)

    def __init__(self, name, unit_price, multiplier=1, id=None):
        # self.id = id
        self.name = name
        self.unit_price = unit_price
        self.multiplier = multiplier

    def serialize(self):
        product_serialized = {
            'id': self.id,
            'name': self.name,
            'unit_price': self.unit_price,
            'multiplier': self.multiplier
        }

        return jsonify(product_serialized)
