from flask import Blueprint, render_template

pedidos_bp = Blueprint('pedido', __name__, url_prefix='/pedidos_feitos')

@pedidos_bp.route('/')
def ver_pedidos_feitos():
    return render_template('pedidos_feitos.html')

@pedidos_bp.route('/editar_pedido')
def editar_pedido_feito():
    return render_template('editar_pedido.html')