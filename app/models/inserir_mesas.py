import json
from app.models.mesa import Mesa
from main import db
from run import app

path = 'app/dados_json/mesas_refatorada.json'

with open(path, encoding='utf-8') as file:
    dados = json.load(file)

itens = []

for item in dados:
    itens.append(Mesa(
        id=item['id'],
        status=item['status'],
    ))

with app.app_context():
    db.create_all()
    try:
        db.session.add_all(itens)
        db.session.commit()
        print("Itens inseridos com sucesso!")
    except Exception as e:
        print("Erro ao inserir:", e)
