from app import db


class SellOrder(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product_amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float(2), nullable=False)
    profitability = db.Column(db.String(50))

    def __init__(self, client, product, product_amount, price, id=None):
        self.id = id
        self.client = client
        self.product = product
        self.product_amount = product_amount
        self.price = price
        self.__set_profitability()

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

