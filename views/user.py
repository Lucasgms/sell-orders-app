from app import app

from models.user import *


@app.route('/user/<id>')
def get_user(id):
    user = User.query.get(id)
    return user.serialize()
