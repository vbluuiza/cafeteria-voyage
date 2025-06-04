from flask import Blueprint, render_template

login_bp = Blueprint('login', __name__, url_prefix='/')

@login_bp.route('/')
def ver_pedidos_feitos():
    return render_template('index.html')