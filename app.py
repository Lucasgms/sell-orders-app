# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
print(os.environ)
app.config.from_object(os.getenv('APP_SETTINGS'))
db = SQLAlchemy(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
