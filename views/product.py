from app import app

from models.product import *


@app.route('/product/<id>')
def get_product(id):
    product = Product.query.get(id)
    return product.serialize()
