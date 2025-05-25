from flask import Blueprint, render_template

item_bp = Blueprint('item', __name__, url_prefix='/item')

@item_bp.route('/')
def ver_item_pedido():
    return render_template('item.html')
