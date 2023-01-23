from ..controllers.HomeController import *

from flask import Blueprint

homeBlueprint = Blueprint('home_bp', __name__)
homeBlueprint.route('', methods=['GET'])(homepage)