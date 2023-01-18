from loader import *
from routes.ServiceRegistryBlueprint import serviceRegistryBlueprint

app.register_blueprint(serviceRegistryBlueprint, url_prefix="/registry")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 80))