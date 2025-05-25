from flask import Blueprint, render_template

confirmar_pedido_bp = Blueprint('pedido', __name__, url_prefix='/pedidos')

@confirmar_pedido_bp.route('/')
def ver_pedido():
    return render_template('pedidos_feitos.html')

