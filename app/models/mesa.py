from main import db

class Mesa(db.Model):
    __tablename__ = 'mesa'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100), nullable=False)
  
    pedidos = db.relationship('Pedido', backref='mesa', lazy=True)
  