from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

from config import Config
# from flask_migrate import Migrate



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize the SQLAlchemy extension
    db.init_app(app)

     # Automatically create the tables if they don't exist
    with app.app_context():
        db.create_all()  # This will create tables based on your models

    # Import routes (after app is created)
    from .routes import main
    app.register_blueprint(main)
    # Migrate(app, db)

    
    return app


