from app import db


class User(db.Model):

    __id = db.Column(db.Integer, primary_key=True)
    __name = db.Column(db.String(120), nullable=False)
    __purchases = db.relationship('SellOrder', backref='user', lazy=True)

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
