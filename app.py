# -*- coding: utf-8 -*-
import os
from flask import Flask
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
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
