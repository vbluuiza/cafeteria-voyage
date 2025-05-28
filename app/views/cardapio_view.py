from flask import Blueprint, render_template, request
from app.models.cardapio import Cardapio
from app.models.pedido import Pedido
from main import db

pratos_bp = Blueprint('pratos', __name__, url_prefix='/cardapio')

@pratos_bp.route('/', methods=["GET", "POST"])
def ver_pratos():
    cardapio = Cardapio.query.all()
    pedido_id = request.args.get("pedido_id", type=int)
    return render_template('cardapio.html', cardapio=cardapio, pedido_id=pedido_id)

@pratos_bp.route('/item/<int:id>')
def ver_item_pedido(id):
    item = Cardapio.query.get_or_404(id)
    
    pedido_id = request.args.get('pedido_id', type=int)
    pedido = Pedido.query.get(pedido_id) if pedido_id else None
        
    return render_template('item.html', item=item,  pedido=pedido)