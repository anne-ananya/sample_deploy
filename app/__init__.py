from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import logging

# Initialize SQLAlchemy and Migrate outside of create_app to avoid reinitialization
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the app with the db and migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Setup console logging for better visibility in production
    if not app.debug:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)

    # Register routes and models (to keep imports local and avoid circular imports)
    with app.app_context():
        from app import routes, models

        # Register the main blueprint for routing
        app.register_blueprint(routes.main)

        # This will ensure that tables are created if not present (though migration is recommended)
        db.create_all()

    # Log app startup
    app.logger.setLevel(logging.INFO)
    app.logger.info('Flask App startup')

    return app
