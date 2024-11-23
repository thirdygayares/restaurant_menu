from flask_smorest import Blueprint
from flask import abort, jsonify

from app.repository.restaurant_repository import RestaurantRepository
from app.schema.restaurant_schema import RestaurantSchema

restaurant_blp = Blueprint('restaurant','restaurant', url_prefix='/restaurant', description="Operation for Restaurant Category")


@restaurant_blp.route("/", methods=['POST'])
@restaurant_blp.arguments(RestaurantSchema)
@restaurant_blp.response(201, RestaurantSchema)
def create_restaurant(data):
    restaurant = RestaurantRepository.create_restaurant(data)
    return restaurant


@restaurant_blp.route("/<string:restaurant_id>", methods=['GET'])
@restaurant_blp.response(200, RestaurantSchema)
def get_restaurant_by_id(restaurant_id):
   restaurant = RestaurantRepository.get_restaurant_by_uuid(restaurant_id)
   if not restaurant:
      return jsonify({"message":"not found"}), 404
   return restaurant

@restaurant_blp.route("/", methods=['GET'])
@restaurant_blp.response(200, RestaurantSchema(many=True))
def get_all_restaurants():
   restaurant = RestaurantRepository.get_all()
   return restaurant


@restaurant_blp.route("/<string:restaurant_id>", methods=['PUT'])
@restaurant_blp.arguments(RestaurantSchema)
@restaurant_blp.response(200, RestaurantSchema)
def update_restaurant(data, restaurant_id):
   restaurant = RestaurantRepository.get_restaurant_by_uuid(restaurant_id)

   if not restaurant:
       abort(404, description="User not found")
   updated_restaurant = RestaurantRepository.update_restaurant(restaurant, data)

   return updated_restaurant

@restaurant_blp.route("/<string:restaurant_id>", methods=["DELETE"])
@restaurant_blp.response(204)
def delete_restaurant(restaurant_id):
   restaurant = RestaurantRepository.get_restaurant_by_uuid(restaurant_id)

   if not restaurant:
      abort(404, description="User Not Found")
   RestaurantRepository.delete_restaurant(restaurant)
   return ''