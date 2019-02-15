# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, flash, redirect, url_for
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


@app.route('/create', methods=['POST'])
def create_order():
    client = User.query.filter_by(id=request.form['client']).first()
    product = Product.query.filter_by(id=request.form['product']).first()
    amount = int(request.form['amount'])
    price = float(request.form['price'])
    order = SellOrder(client, product, amount, price)
    client.purchases.append(order)
    product.sell_orders.append(order)
    db.session.add(client)
    db.session.add(product)
    db.session.add(order)
    db.session.commit()

    flash('Ordem de venda cadastrada com sucesso!')
    return redirect(url_for('index'))


@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.filter_by(id=id).first()
    return product.serialize()


@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    return user.serialize()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
