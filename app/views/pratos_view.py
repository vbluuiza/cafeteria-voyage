from flask import Blueprint, render_template

pratos_bp = Blueprint('pratos', __name__, url_prefix='/pratos')

@pratos_bp.route('/')
def ver_pratos():
    return render_template('index.html')

@pratos_bp.route('/item')
def ver_item_pedido():
    return render_template('item.html')