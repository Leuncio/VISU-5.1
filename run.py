from the_app import create_app
from the_app.db_setup import insert_default_data
from the_app.coordenadas import load_data

app = create_app()

with app.app_context():
    insert_default_data()
    semaforos, agvs = load_data()

if __name__ == "__main__":
    app.run(debug=True, port=3030)
