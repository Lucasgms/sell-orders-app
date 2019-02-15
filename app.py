# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETINGS'))
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models.product import *
from models.user import *
from models.sell_order import *


@app.route('/')
def index():
    sell_orders = SellOrder.query.all()
    return render_template('list.html', title="Ordens de compra", orders=sell_orders)


@app.route('/new')
def new_order():
    users = User.query.all()
    products = Product.query.all()

    return render_template('new.html', title="Nova ordem de compra", clients=users, products=products)


@app.route('/create')
def create_order():
    pass


@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.filter_by(id=id).first()
    return jsonify(product.serialize)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
