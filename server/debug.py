#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

if __name__ == '__main__':
    with app.app_context(): # type: ignore
        import ipdb; ipdb.set_trace() # type: ignore