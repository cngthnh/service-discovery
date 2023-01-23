from core.loader import *
from core.routes.ServiceRegistryBlueprint import serviceRegistryBlueprint
from core.routes.HomeBlueprint import homeBlueprint
from core.models import Service, SUSPENDED_SERVICE_THRESHOLD, DEAD_SERVICE_THRESHOLD, SQLAlchemyError, ServiceStatus
from datetime import datetime, timedelta

app.register_blueprint(homeBlueprint, url_prefix="/")
app.register_blueprint(serviceRegistryBlueprint, url_prefix="/registry")

@app.lib.cron()
def inactiveNodeChecker(event):
    print(event)
    now = datetime.utcnow()
    deadTime = now - timedelta(minutes=DEAD_SERVICE_THRESHOLD)
    suspendedTime = now - timedelta(minutes=SUSPENDED_SERVICE_THRESHOLD)
    with app.app_context():
        try:
            db.session.query(Service).filter(Service.last_heartbeat < suspendedTime).update({"status": ServiceStatus.SUSPENDED.value})
            db.session.query(Service).filter(Service.last_heartbeat < deadTime).delete()
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 80))