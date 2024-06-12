#!/usr/bin/python3xx
'''api status'''
from flask import jsonify
from models import storage
from . import app_views
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

@app_views.route("/status", methods=["GET"])
def status():
    """Return status OK"""
    return jsonify({"status": "OK"})

@app_views.route("/stats", methods=["GET"])
def stats():
    """Return statistics about the number of each object type"""
    stats = {
        "states": storage.count(State),
        "users": storage.count(User),
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review)
    }
    return jsonify(stats)
