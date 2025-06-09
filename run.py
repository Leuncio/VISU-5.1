from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    db.create_all()  # 🔹 Creates all bound databases

if __name__ == "__main__":
    app.run(debug=True, port=3030)
