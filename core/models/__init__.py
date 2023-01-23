from ..loader import db, app
from sqlalchemy.exc import SQLAlchemyError
from .Service import ServiceStatus, Service, SUSPENDED_SERVICE_THRESHOLD, DEAD_SERVICE_THRESHOLD
import sys

with app.app_context():
    try:
        db.create_all()
        db.session.commit()
    except Exception as e:
        print(str(e))
        sys.stdout.flush()
        db.session.rollback()