from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizzas.db"
db = SQLAlchemy(app)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(100), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', lazy=True)

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __init__(self, price, pizza_id, restaurant_id):
        self.price = price
        self.pizza_id = pizza_id
        self.restaurant_id = restaurant_id

    def to_dict(self):
        return {
            "id": self.id,
            "pizza": self.pizza.to_dict(),
            "pizza_id": self.pizza_id,
            "price": self.price,
            "restaurant": self.restaurant.to_dict(),
            "restaurant_id": self.restaurant_id
        }

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(restaurant.to_dict())

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid request"}), 400
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    if price is None or pizza_id is None or restaurant_id is None:
        return jsonify({"error": "Invalid request"}), 400
    if price < 1 or price > 30:
        return jsonify({"errors": ["price must be between 1 and 30"]}), 400
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)
    if pizza is None or restaurant is None:
        return jsonify({"error": "Invalid request"}), 400
    restaurant_pizza = RestaurantPizza(price, pizza_id, restaurant_id)
    db.session.add(restaurant_pizza)
    db.session.commit()
    return jsonify(restaurant_pizza.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)