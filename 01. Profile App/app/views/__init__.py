from flask import Blueprint

public_app = Blueprint("public_app", __name__)

from . import public