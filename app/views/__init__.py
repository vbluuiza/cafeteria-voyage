from .initial_view import login_bp
from .cardapio_view import pratos_bp
from .pedidos_view import pedidos_bp

def registrar_blueprints(app):
    app.register_blueprint(login_bp)
    app.register_blueprint(pratos_bp)
    app.register_blueprint(pedidos_bp)
