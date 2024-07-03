from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade='all, delete-orphan')
     
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'restaurant_pizzas': [rp.to_dict() for rp in self.restaurant_pizzas]
        }
from app import db

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }
class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'pizza': self.pizza.to_dict(),
            'pizza_id': self.pizza_id,
            'price': self.price,
            'restaurant': self.restaurant.to_dict(),
            'restaurant_id': self.restaurant_id
        }

    def __init__(self, price, pizza_id, restaurant_id):
        self.price = price
        self.pizza_id = pizza_id
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return f'RestaurantPizza({self.id}, {self.price}, {self.pizza_id}, {self.restaurant_id})'