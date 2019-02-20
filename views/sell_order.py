from flask import Flask, render_template, request, flash, redirect, url_for
from app import db, app
from models.product import *
from models.user import *
from models.sell_order import *


@app.route('/')
def index():
    sell_orders = SellOrder.query.all()
    return render_template('list.html', title="Pedidos", orders=sell_orders)


@app.route('/order/new')
def new_order():
    users = User.query.all()
    products = Product.query.all()

    return render_template('new.html', title="Novo Pedido", clients=users, products=products)


@app.route('/order/save', methods=['POST'])
def save_order():
    client = User.query.get(request.form['client'])
    product = Product.query.get(request.form['product'])
    amount = int(request.form['amount'])
    price = float(request.form['price'])

    if request.form.get('id'):
        order = SellOrder.query.get(request.form['id'])
        order.client = client
        order.product = product
        order.product_amount = amount
        order.price = price
        order.set_profitability()
    else:
        order = SellOrder(client, product, amount, price)

    client.purchases.append(order)
    product.orders.append(order)
    db.session.add(client)
    db.session.add(product)
    db.session.commit()
    db.session.flush()

    flash('Pedido cadastrado com sucesso!')
    return redirect(url_for('index'))


@app.route('/order/edit/<id>')
def edit_order(id):
    users = User.query.all()
    products = Product.query.all()
    sell_order = SellOrder.query.get(id)

    return render_template('new.html', title="Editar pedido", clients=users, products=products, sell_order=sell_order)


@app.route('/order/delete/<id>')
def delete_order(id):
    sell_order = SellOrder.query.get(id)
    db.session.delete(sell_order)
    db.session.commit()

    flash('Pedido excluído com sucesso!')
    return redirect(url_for('index'))
