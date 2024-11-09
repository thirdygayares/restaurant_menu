from flask import Flask, jsonify
from flask_smorest import Api

from app.blueprint.user_blueprint import user_blp
from app.extension import db, migrate
from config import Config
from app.models import user_model

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app)
    api.register_blueprint(user_blp)


    @app.route('/')
    def home():
        return jsonify({"message": "Hello Worldssss"})

    return app