class Restaurant(db.Model):
    # ... (rest of the class definition)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'restaurant_pizzas': [rp.to_dict() for rp in self.restaurant_pizzas]
        }

class Pizza(db.Model):
    # ... (rest of the class definition)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
            'restaurant_pizzas': [rp.to_dict() for rp in self.restaurant_pizzas]
        }

class RestaurantPizza(db.Model):
    # ... (rest of the class definition)

    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'restaurant_id': self.restaurant_id,
            'pizza_id': self.pizza_id,
            'restaurant': self.restaurant.to_dict() if self.restaurant else None,
            'pizza': self.pizza.to_dict() if self.pizza else None
        }