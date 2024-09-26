from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

from .config.config import Config
from .handlers.error_handler import handle_400_error ,handle_404_error




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
    from .views.routes import task_bp
    app.register_blueprint(task_bp)
    # Migrate(app, db)

    app.register_error_handler(404, handle_404_error)
    app.register_error_handler(400, handle_400_error)

    
    return app


