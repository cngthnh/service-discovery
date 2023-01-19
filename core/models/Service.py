from ..loader import db
from datetime import datetime
from enum import Enum

class ServiceStatus(Enum):
    HEALTHY = 1
    SERVICE_DOWN = 2
    SUSPENDED = 3
    WATCHER_DOWN = 4

class Service(db.Model):
    __tablename__ = 'service'
    name = db.Column(db.UnicodeText, primary_key = True)
    url = db.Column(db.Text, primary_key = True)
    status = db.Column(db.Integer, default = ServiceStatus.HEALTHY.value)
    last_heartbeat = db.Column(db.DateTime, default = datetime.utcnow)
    latency = db.Column(db.BigInteger, default = 0)
    created_time = db.Column(db.DateTime, default = datetime.utcnow)
    updated_time = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    def __init__(self, name, url):
        self.name = name
        self.url = url
    
    def toDict(self):
        result = {
            "name": self.name,
            "url": self.url,
            "status": ServiceStatus(self.status).name,
            "last_heartbeat": self.last_heartbeat.isoformat(),
            "created_time": self.created_time.isoformat(), 
            "updated_time": self.updated_time.isoformat()
        }
        return result