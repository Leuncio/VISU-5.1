# run.py

from the_app import create_app
from the_app.converciones import dbs_para_dict  # opcional: só para forçar leitura inicial (testes/debug)

app = create_app()

with app.app_context():
    # Força a leitura dos dados do banco no início (opcional)
    dados = dbs_para_dict()
    print("Dados carregados ao iniciar o servidor.")

if __name__ == "__main__":
    app.run(debug=True, port=3030)
