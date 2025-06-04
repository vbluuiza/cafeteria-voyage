from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app.config.config_dev import ConfigDev
import os
from unidecode import unidecode

load_dotenv()

db = SQLAlchemy()

def criar_app():
    app = Flask(
        __name__,
        template_folder='app/templates',
        static_folder='app/static'
    )
    
    app.config.from_object(ConfigDev)
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
    db_path = os.path.join(root_path, 'instance', 'cafeteria.db')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///cafeteria.db"

    db.init_app(app)

    @app.template_filter('normalize_nome')
    def normalize_nome(nome):
        return unidecode(nome.lower().replace(" ", "_").replace("ã", "a").replace("ç", "c"))

    from app.models import mesa, cardapio, item_pedido, pedido 
    from app.views import registrar_blueprints
    registrar_blueprints(app)

    return app
