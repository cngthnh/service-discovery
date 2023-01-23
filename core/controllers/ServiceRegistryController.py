from ..loader import *
from ..models.Service import Service, ServiceStatus
from flask import request, jsonify
from datetime import datetime
import json
from sqlalchemy import exc
import requests
from datetime import timedelta

def register():
    _last_heartbeat = datetime.utcnow()
    try:
        data = request.get_json()
        _name = str(data["name"])
        _url = str(data["url"])
    except Exception:
        return jsonify(message="Invalid data"), 400

    _status = None
    # ping back
    try: 
        response = requests.get(_url)
        if response.ok:
            _status = ServiceStatus.HEALTHY.value
            _latency = int(response.elapsed / timedelta(milliseconds=1))
        else:
            _status = ServiceStatus.SERVICE_DOWN.value
            _latency = -1
    except Exception as e:
        print(e)
        return jsonify(message="Invalid URL"), 400

    service = db.session.query(Service).filter_by(name = _name, url = _url).first()
    if (service is None):
        service = Service(_name, _url)

    service.last_heartbeat = _last_heartbeat
    service.status = _status
    service.latency = _latency
    try:
        db.session.add(service)
        db.session.commit()
    except Exception as e:
        return "Invalid data", 400

    return "Registered", 201

def getServices():
    allServices = db.session.query(Service).order_by(Service.last_heartbeat.desc(), Service.status).all()
    serviceDict = []
    for service in allServices:
        serviceDict.append(service.toDict())
    result = {
        "result": "OK",
        "count": len(serviceDict),
        "services": serviceDict
    }
    
    return json.dumps(result), 200