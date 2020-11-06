from flask import Flask, jsonify, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import config
from contextlib import closing
import sqlite3
import nw_logging

def create_app():

    app = Flask(__name__)

    import flaskr_routes
    app.register_blueprint(flaskr_routes.bp)

    return app