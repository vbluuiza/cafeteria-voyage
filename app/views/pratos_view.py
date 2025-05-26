from flask import Blueprint, render_template
pratos_bp = Blueprint('pratos', __name__, url_prefix='/pratos')

@pratos_bp.route('/')
def ver_pratos():
    cardapio = Cardapio.query.all()
    return render_template('index.html', cardapio=cardapio)

@pratos_bp.route('/item')
def ver_item_pedido():
    return render_template('item.html')