# run.py

from the_app import create_app
from the_app.converciones import dbs_para_dict 

app = create_app()

with app.app_context():

    dados = dbs_para_dict()

if __name__ == "__main__":
    app.run(debug=True, port=3030)
