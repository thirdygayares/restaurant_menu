from flask import abort, jsonify
from flask_smorest import Blueprint
from app.repository.user_repository import UserRepository
from app.schema.user_schema import UserSchema

user_blp = Blueprint('users','users', url_prefix='/users', description="Operation for users")

@user_blp.route("/", methods=['POST'])
@user_blp.arguments(UserSchema)
@user_blp.response(201, UserSchema)
def create_user(data):
   user = UserRepository.create_user(data)
   return user

@user_blp.route("/<int:user_id>", methods=['GET'])
@user_blp.response(200, UserSchema)
def get_user_by_id(user_id):
   user = UserRepository.get_user_by_id(user_id)
   if not user:
      return jsonify({"message":"not found"}), 404
   return user



