from unittest import TestCase

from models.product import Product
from models.sell_order import SellOrder
from models.user import User


class TestSellOrder(TestCase):
    def test___set_profitability_great(self):
        client = User('Lucas')
        product = Product('Product 1', 100.0, 0)
        sell_order = SellOrder(client, product, 1, 100.1)
        client.purchases.append(sell_order)
        product.sell_orders.append(sell_order)

        assert sell_order.profitability == 'Ótima'

    def test___set_profitability_good_1(self):
        client = User('Lucas')
        product = Product('Product 1', 100.0, 0)
        sell_order = SellOrder(client, product, 1, 100.0)
        client.purchases.append(sell_order)
        product.sell_orders.append(sell_order)

        assert sell_order.profitability == 'Boa'

    def test___set_profitability_good_2(self):
        client = User('Lucas')
        product = Product('Product 1', 100.0, 0)
        sell_order = SellOrder(client, product, 1, 90.0)
        client.purchases.append(sell_order)
        product.sell_orders.append(sell_order)

        assert sell_order.profitability == 'Boa'

    def test___set_profitability_bad(self):
        client = User('Lucas')
        product = Product('Product 1', 100.0, 0)
        sell_order = SellOrder(client, product, 1, 89.9)
        client.purchases.append(sell_order)
        product.sell_orders.append(sell_order)

        assert sell_order.profitability == 'Ruim'
