from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.config_dev import ConfigDev

db = SQLAlchemy()

def criar_app():
    app = Flask(__name__)
    app.config.from_object(ConfigDev)

    db.init_app(app)
    
    from app.models import mesa, cardapio, item_pedido, pedido

    return app

