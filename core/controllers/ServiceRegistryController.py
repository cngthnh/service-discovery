from ..loader import *
from ..models.Service import Service
from flask import request, jsonify
from datetime import datetime
import json
from sqlalchemy import exc

def register():
    _last_heartbeat = datetime.utcnow()
    try:
        data = request.get_json()
        _name = str(data["name"])
        _url = str(data["url"])
    except Exception:
        return jsonify(message="Invalid data"), 400
    
    service = db.session.query(Service).filter_by(name = _name, url = _url).first()
    if (service is None):
        service = Service(_name, _url, _last_heartbeat)
    try:
        db.session.add(service)
        db.session.commit()
    except Exception as e:
        return "Invalid data", 400

    return "Registered", 201

def getServices():
    allServices = db.session.query(Service).all()
    result = []
    for service in allServices:
        result.append(service.toDict())
    
    return json.dumps(result), 200