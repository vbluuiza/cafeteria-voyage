from main import db
class Cardapio(db.Model):
    __tablename__ = 'cardapio'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(300), nullable=True)
    ingredientes = db.Column(db.String(300), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    subcategoria = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)

    