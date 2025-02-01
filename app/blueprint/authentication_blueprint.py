
from flask import jsonify
from flask_smorest import Blueprint

from app.schema.login_schema import LoginSchema
from app.service.authentication_service import AuthenticationService

auth_blp = Blueprint('auth', 'auth', url_prefix='/auth', description="Authentication")

@auth_blp.route("/login", methods=["POST"])
@auth_blp.arguments(LoginSchema)
def login(data):
    email = data.get("email")
    password = data.get("password")

    token, error = AuthenticationService.authenticate_user(email, password)

    if error:
        return jsonify({"message":error}), 401

    return jsonify(token), 200
