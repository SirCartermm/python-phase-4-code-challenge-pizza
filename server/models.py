from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True, cascade='all, delete')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', lazy=True, cascade='all, delete')

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant = db.relationship('Restaurant', backref=db.backref('restaurant_pizzas', lazy=True, cascade='all, delete'))
    pizza = db.relationship('Pizza', backref=db.backref('restaurant_pizzas', lazy=True, cascade='all, delete'))