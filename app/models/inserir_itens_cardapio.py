import json
from app.models.cardapio import Cardapio
from main import db
from run import app

path = 'app/dados_json/cardapio_refatorado.json'

with open(path, encoding='utf-8') as file:
    dados = json.load(file)

itens = []

for item in dados:
    itens.append(Cardapio(
        id=item['id'],
        nome=item['nome'],
        descricao=item['descricao'],
        ingredientes=item['ingredientes'],
        preco=item['preco'],
        opcionais=item.get('opcionais', []),
        subcategoria=item['subcategoria'],
        categoria=item['categoria']
    ))

with app.app_context():
    db.create_all()
    try:
        db.session.add_all(itens)
        db.session.commit()
        print("Itens inseridos com sucesso!")
    except Exception as e:
        print("Erro ao inserir:", e)

