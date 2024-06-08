from flask import Flask
from config import Config
from models import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
