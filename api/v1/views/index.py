#!/usr/bin/python3
'''api status'''

from flask import jsonify
from . import app_views


@app_views.route("/status", methods=["GET"])
def status():
    """Return status OK"""
    return jsonify({"status": "OK"})
