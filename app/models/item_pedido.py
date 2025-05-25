from main import db

class ItemPedido(db.Model):
    __tablename__ = 'item_pedido'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    cardapio_id = db.Column(db.Integer, db.ForeignKey('cardapio.id'), nullable=True)
    quantidade = db.Column(db.String(300), nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)

    cardapio = db.relationship('Cardapio', backref='itens_pedido')  
    