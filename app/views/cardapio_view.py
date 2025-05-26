from flask import Blueprint, render_template
from app.models.cardapio import Cardapio

pratos_bp = Blueprint('pratos', __name__, url_prefix='/cardapio')

@pratos_bp.route('/')
def ver_pratos():
    cardapio = Cardapio.query.all()
    return render_template('cardapio.html', cardapio=cardapio)

@pratos_bp.route('/item')
def ver_item_pedido():
    return render_template('item.html')
