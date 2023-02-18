from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from raw_data import *
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)

    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Offer(db.Model):
    __tablename__ = 'offer'

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


with app.app_context():
    db.create_all()

    for user in users:
        db.session.add(User(**user))
        db.session.commit()

    for order in orders:
        order['start_date'] = datetime.strptime(order['start_date'], '%m/%d/%Y').date()
        order['end_date'] = datetime.strptime(order['end_date'], '%m/%d/%Y').date()

        db.session.add(Order(**order))
        db.session.commit()

    for _ in offers:
        db.session.add(Offer(**_))
        db.session.commit()


@app.route('/user/<int:uid>', methods=['GET', 'DELETE', 'PUT'])
def users(uid):
    if request.method == 'GET':
        user = User.query.get(uid).to_dict()
        return jsonify(user)
    if request.method == 'DELETE':
        user = User.query.get(uid)
        db.session.delete(user)
        db.session.commit()
        return '', 202
    if request.method == 'PUT':
        user_data = request.json
        user = User.query.get(uid)

        if user_data.get('first_name'):
            user.first_name = user_data['first_name']
        if user_data.get('last_name'):
            user.last_name = user_data['last_name']
        if user_data.get('age'):
            user.age = user_data['age']
        if user_data.get('email'):
            user.email = user_data['email']
        if user_data.get('role'):
            user.role = user_data['role']
        if user_data.get('phone'):
            user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()
        return '', 202


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])
    if request.method == 'POST':
        user_data = request.json
        db.session.add(User(**user_data))
        db.session.commit()
        return '', 201


@app.route('/order/<int:uid>', methods=['GET', 'DELETE', 'PUT'])
def order(uid):
    if request.method == 'GET':
        order = Order.query.get(uid).to_dict()
        return jsonify(order)
    if request.method == 'DELETE':
        order = Order.query.get(uid)
        db.session.delete(order)
        db.session.commit()
        return '', 202


@app.route('/order', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        orders = Order.query.all()
        return jsonify([order.to_dict() for order in orders])
    if request.method == 'POST':
        order_data = request.json
        db.session.add(User(**order_data))
        db.session.commit()
        return '', 201


@app.route('/offer/<int:uid>', methods=['GET', 'DELETE', 'PUT'])
def offer(uid):
    if request.method == 'GET':
        offer = Offer.query.get(uid).to_dict()
        return jsonify(offer)
    if request.method == 'DELETE':
        offer = Offer.query.get(uid)
        db.session.delete(offer)
        db.session.commit()
        return '', 202



@app.route('/offer', methods=['GET', 'POST'])
def offers():
    if request.method == 'GET':
        offers = Offer.query.all()
        return jsonify([offer.to_dict() for offer in offers])
    if request.method == 'POST':
        offer_data = request.json
        db.session.add(User(**offer_data))
        db.session.commit()
        return '', 201



if __name__ == '__main__':
    app.run()
