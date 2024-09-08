from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from celery import Celery
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize extensions at the top
db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO(async_mode='eventlet')

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions with the app
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    # Import routes only after initializing extensions to avoid circular import
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    return celery
