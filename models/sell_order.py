from app import db


class SellOrder(db.Model):

    __id = db.Column(db.Integer, primary_key=True)
    __client = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    __product = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    __product_amount = db.Column(db.Integer, nullable=False)
    __price = db.Column(db.Float(2), nullable=False)
    __profitability = db.Column(db.String(50))

    def __init__(self, client, product, product_amount, price, id=None):
        self.id = id
        self.client = client
        self.product = product
        self.product_amount = product_amount
        self.price = price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, client):
        self.__client = client

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product):
        self.__product = product

    @property
    def product_amount(self):
        return self.__product_amount

    @product_amount.setter
    def product_amount(self, product_amount):
        self.__product_amount = product_amount

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def profitability(self):
        return self.__profitability

    def __set_profitability(self):
        price_range = (self.price / self.product.unit_price) * 100
        price_range_start = self.product.unit_price - (self.product.unit_price / 10) * 100
        price_range_end = self.product.unit_price + (self.product.unit_price / 10) * 100

        if self.price > self.product.unit_price:
            self.__profitability = 'Ótima'
        elif price_range in range(price_range_start, price_range_end):
            self.__profitability = 'Boa'
        else:
            self.__profitability = 'Ruim'

