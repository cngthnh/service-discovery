from ..loader import db
from Service import Service
import sys

try:
    db.create_all()
    db.session.commit()
except Exception as e:
    print(str(e))
    sys.stdout.flush()
    db.session.rollback()