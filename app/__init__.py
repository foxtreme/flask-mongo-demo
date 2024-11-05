from flask import Flask
from config import Config
from flask_pymongo import PyMongo


mongo = PyMongo()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    from app.resources.room_resource import bp as rooms_bp
    app.register_blueprint(rooms_bp)
    return app
