from flask import Flask, jsonify
from flask_cors import CORS
from flask_smorest import Api

from app.blueprint.authentication_blueprint import auth_blp
from app.blueprint.menu_blueprint import menu_blp
from app.blueprint.menu_category_blueprint import menu_category_blp
from app.blueprint.restaurant_blueprint import restaurant_blp
from app.blueprint.restaurant_category_blueprint import restaurant_category_blp
from app.blueprint.user_blueprint import user_blp
from app.extension import db, migrate, bcrypt, jwt
from config import Config
from app.models import user_model
from app.models import restaurant_category_model
from app.models import menu_category_model
from app.models import restaurant_model
from app.models import menu_model

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    api = Api(app)
    api.register_blueprint(user_blp)
    api.register_blueprint(restaurant_category_blp)
    api.register_blueprint(menu_category_blp)
    api.register_blueprint(restaurant_blp)
    api.register_blueprint(menu_blp)
    api.register_blueprint(auth_blp)


    @app.route('/')
    def home():
        return jsonify({"message": "Hello World"})

    return app