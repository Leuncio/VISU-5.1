# run.py

from app import create_app  # Import the create_app function to initialize the Flask application


app = create_app()  # Create the Flask application instance



if __name__ == "__main__":
    app.run(debug=True, port=3030)
