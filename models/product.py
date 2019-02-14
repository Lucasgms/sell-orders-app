from app import db


class Product(db.Model):

    __id = db.Column(db.Integer, primary_key=True)
    __name = db.Column(db.String(120), nullable=False)
    __unit_price = db.Column(db.Float(2), nullable=False)
    __multiplier = db.Column(db.Integer)
    __sell_orders = db.relationship('SellOrder', backref='product', lazy=True)

    def __init__(self, name, unit_price, multiplier, id=None):
        self.id = id
        self.name = name
        self.unit_price = unit_price
        self.multiplier = multiplier

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def unit_price(self):
        return self.__unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        self.__unit_price = unit_price

    @property
    def multiplier(self):
        return self.__multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        self.__multiplier = multiplier
