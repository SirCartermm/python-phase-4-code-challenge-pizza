from flask import Blueprint, request, jsonify
from server.models import Restaurant, Pizza, RestaurantPizza

bp = Blueprint('api', _name_)

@bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants])

@bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404
    return jsonify(restaurant.to_dict())