# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from views.user import *
from views.product import *
from views.sell_order import *


if __name__ == '__main__':
    app.run(host='0.0.0.0')
