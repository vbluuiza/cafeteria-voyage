from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.config_dev import ConfigDev

db = SQLAlchemy()

def criar_app():
    app = Flask(__name__,
                template_folder='app/templates',
                static_folder='app/static'
                )
    app.config.from_object(ConfigDev)

    db.init_app(app)
    
    from app.models import mesa, cardapio, item_pedido, pedido 
    from app.views import registrar_blueprints
    registrar_blueprints(app)

    return app

