#!/usr/bin/env python3
from models import db, Restaurant, RestaurantPizza, Pizza
from flask_migrate import Migrate # type: ignore
from flask import Flask, request, make_response # type: ignore
