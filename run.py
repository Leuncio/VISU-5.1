from app import create_app
from app.db_setup import insert_default_data

app = create_app()

# ✅ Run database setup inside Flask context
with app.app_context():
    insert_default_data()

if __name__ == "__main__":
    app.run(debug=True, port=3030)
