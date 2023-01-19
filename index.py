from core.loader import *
from core.routes.ServiceRegistryBlueprint import serviceRegistryBlueprint
from core.routes.HomeBlueprint import homeBlueprint

app.register_blueprint(homeBlueprint, url_prefix="/")
app.register_blueprint(serviceRegistryBlueprint, url_prefix="/registry")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 80))