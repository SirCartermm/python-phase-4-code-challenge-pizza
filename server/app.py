from flask import jsonify, request
from server import app, db # type: ignore
from server.models import Restaurant, Pizza, RestaurantPizza

@app.route('/restaurants', methods=['GET']) # type: ignore
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET']) # type: ignore
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        return jsonify(restaurant.to_dict())
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app.route('/restaurants/<int:id>', methods=['DELETE']) # type: ignore
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({}), 204
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app.route('/pizzas', methods=['GET']) # type: ignore
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict() for p in pizzas])

@app.route('/restaurant_pizzas', methods=['POST']) # type: ignore
def create_restaurant_pizza():
    data = request.get_json()
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    price = data.get('price')
    if pizza_id and restaurant_id and price:
        restaurant_pizza = RestaurantPizza(restaurant_id=restaurant_id, pizza_id=pizza_id, price=price) # type: ignore
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(restaurant_pizza.to_dict()), 201
    else:
        return jsonify({'errors': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(debug=True) # type: ignore