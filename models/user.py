from flask import jsonify
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    purchases = db.relationship('SellOrder', backref='user', lazy=True)

    def __init__(self, name, id=None):
        # self.id = id
        self.name = name

    def serialize(self):
        user_serialized = {
            'id': self.id,
            'name': self.name,
            'purchases': self.purchases
        }

        return jsonify(user_serialized)
