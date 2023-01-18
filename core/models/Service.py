from ..loader import db
from datetime import datetime

class Service(db.Model):
    __tablename__ = 'service'
    name = db.Column(db.UnicodeText, primary_key = True)
    url = db.Column(db.Text, primary_key = True)
    last_heartbeat = db.Column(db.DateTime, default = datetime.utcnow)
    created_time = db.Column(db.DateTime, default = datetime.utcnow)
    updated_time = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    def __init__(self, name, url, last_hearbeat):
        self.name = name
        self.url = url
        self.last_heartbeat
    
    def toDict(self):
        result = {
            "name": self.name,
            "url": self.url,
            "last_heartbeat": self.last_heartbeat.isoformat(),
            "created_time": self.created_time.isoformat(), 
            "updated_time": self.updated_time.isoformat()
        }
        return result