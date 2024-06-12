#!/usr/bin/python3
'''api status'''
from flask import jsonify
from api.v1.views import app_views
from models import storage, State, User, Amenity, City, Place, Review

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def returnstuff():
    '''return stuff'''
    return jsonify(status='OK')

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stuff():
    '''JSON Responses'''
    todos = {'states': State, 'users': User,
            'amenities': Amenity, 'cities': City,
            'places': Place, 'reviews': Review}
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)
