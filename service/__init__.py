from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    # Security headers using Talisman
    Talisman(app, force_https=False)

    return app
