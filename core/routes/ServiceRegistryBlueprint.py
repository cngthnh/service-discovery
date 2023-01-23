from ..controllers.ServiceRegistryController import *

from flask import Blueprint

serviceRegistryBlueprint = Blueprint('service_registry_bp', __name__)
serviceRegistryBlueprint.route('', methods=['GET'])(getServices)
serviceRegistryBlueprint.route('', methods=['POST'])(register)