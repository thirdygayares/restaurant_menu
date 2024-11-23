from flask import jsonify, make_response
from flask_jwt_extended import set_access_cookies, jwt_required, get_jwt_identity, unset_jwt_cookies, get_jwt
from flask_smorest import Blueprint
from app.schema.login_schema import LoginSchema
from app.service.authentication_service import AuthenticationService

auth_blp = Blueprint('auth', 'auth', url_prefix='/auth', description="Operations for authentication")

@auth_blp.route("/login", methods=['POST'])
@auth_blp.arguments(LoginSchema)
def login(data):
    email = data.get("email")
    password = data.get("password")

    tokens, error = AuthenticationService.authenticate_user(email, password)

    access_token = tokens["access_token"]

    response = make_response(jsonify({"message": "Login successful"}))
    set_access_cookies(response, access_token)

    return response

@auth_blp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()

    claims = get_jwt()

    return jsonify({
        "user_id": current_user_id,
        "email": claims.get("email"),
        "role": claims.get("role")
    }), 200

@auth_blp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    response = make_response(jsonify({"message": "Logout successful"}))
    unset_jwt_cookies(response)
    return response