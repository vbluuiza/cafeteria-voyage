from main import db

class Pedido(db.Model):
    __tablename__ = 'pedido'
    id = db.Column(db.Integer, primary_key=True)
    mesa_id = db.Column(db.Integer, db.ForeignKey('mesa.id') ,nullable=False)
    preco_total = db.Column(db.Float, nullable=False)
    observacao = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
  
    mesa = db.relationship('Mesa', back_populates='pedidos')
    itens = db.relationship('ItemPedido', backref='pedido', cascade="all, delete")