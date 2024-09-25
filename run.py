from app import create_app
import os
# from flask_migrate import Migrate
# from app.models import db  # Assuming models and db are in app.models


app = create_app()

# Setup Flask-Migrate to handle migrations
#migrate = Migrate(app, db)

if __name__ == '__main__':
    print("Database URI:", os.getenv('DATABASE_URL'))
    app.run()
