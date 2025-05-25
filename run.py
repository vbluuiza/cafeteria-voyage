from main import criar_app,db
from flask import Flask

app = criar_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()