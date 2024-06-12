# api/v1/views/__init__.py

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

# Wildcard import, ignore PEP8 warning
from api.v1.views.index import *
