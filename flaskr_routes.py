from flask import Blueprint
from gems_modbus import GemsModbus

from flask import Flask, jsonify, redirect, url_for, request
from sqlalchemy import and_, func
import json
import psutil
from datetime import datetime, time, timedelta

#Reference: https://stackoverflow.com/questions/57726047/sqlalchemy-expression-language-and-sqlites-on-delete-cascade
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection
import subprocess
import nw_logging
import requests

SLAVE = 1
MAP_ADDRESS = 137

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def ninewatt_hello():
    return "welcome ninewatt"

@bp.route('/polling')
def get_modbus_value():
    try:
        raw_modbus_value = round(GemsModbus.read_device_map(SLAVE, MAP_ADDRESS) * 2.2, 2) #0.01 * 220v
        url_txt = "https://emoncms.org/input/post?node=testNode&fulljson={%22power1%22:" + str(raw_modbus_value) + "}&apikey=2269414fd08c61774b00680cfda682ed"
        res = requests.get(url_txt, timeout=10)
        print(res.text)
        return jsonify(success=True)
            
    except Exception as e:
        nw_logging._LOGGER.error(e)
        print(e)
        return jsonify({'error': 'get Modbus Value'}), 500