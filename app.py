# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETINGS'))
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.product import Product
from models.user import User
from models.sell_order import SellOrder


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
