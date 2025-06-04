from main import criar_app,db
from flask import Flask
import os 

os.makedirs("instance", exist_ok=True)

app = criar_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=10000)