from .pratos_view import pratos_bp
from .confirmar_pedido_view import confirmar_pedido_bp

def registrar_blueprints(app):
    app.register_blueprint(pratos_bp)
    app.register_blueprint(confirmar_pedido_bp)
