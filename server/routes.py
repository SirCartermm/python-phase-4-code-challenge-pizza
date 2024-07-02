from flask import Blueprint, request, jsonify
from server.models import Restaurant, Pizza, RestaurantPizza

bp = Blueprint('api', _name_)

@bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants])