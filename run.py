# run.py

from app import create_app  # Import the create_app function to initialize the Flask application
from app.models import db

app = create_app()  # Create the Flask application instance

# Ensure the database tables are created
with app.app_context():
    db.create_all()



if __name__ == "__main__":
    app.run(debug=True, port=3030)
