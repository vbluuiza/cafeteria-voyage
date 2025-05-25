import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
class ConfigDev:
    DEBUG = True

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = "sqlite:///cafeteria.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False