from flask_smorest import Blueprint
from flask import abort, jsonify

from app.repository.restaurant_category_repository import RestaurantCategoryRepository
from app.schema.restaurant_category_schema import RestaurantCategorySchema

restaurant_category_blp = Blueprint('restaurant_category','restaurant_category', url_prefix='/restaurant-category', description="Operation for Restaurant Category")


@restaurant_category_blp.route("/", methods=['POST'])
@restaurant_category_blp.arguments(RestaurantCategorySchema)
@restaurant_category_blp.response(201, RestaurantCategorySchema)
def create_restaurant_category(data):
    restaurant_category = RestaurantCategoryRepository.create_restaurant_category(data)
    return restaurant_category


@restaurant_category_blp.route("/<string:restaurant_category_id>", methods=['GET'])
@restaurant_category_blp.response(200, RestaurantCategorySchema)
def get_restaurant_category_by_id(restaurant_category_id):
   restaurant_category = RestaurantCategoryRepository.get_restaurant_category_by_uuid(restaurant_category_id)
   if not restaurant_category:
      return jsonify({"message":"not found"}), 404
   return restaurant_category

@restaurant_category_blp.route("/", methods=['GET'])
@restaurant_category_blp.response(200, RestaurantCategorySchema(many=True))
def get_all_restaurant_categorys():
   restaurant_category = RestaurantCategoryRepository.get_all()
   return restaurant_category


@restaurant_category_blp.route("/<string:restaurant_category_id>", methods=['PUT'])
@restaurant_category_blp.arguments(RestaurantCategorySchema)
@restaurant_category_blp.response(200, RestaurantCategorySchema)
def update_restaurant_category(data, restaurant_category_id):
   restaurant_category = RestaurantCategoryRepository.get_restaurant_category_by_uuid(restaurant_category_id)

   if not restaurant_category:
       abort(404, description="User not found")
   updated_restaurant_category = RestaurantCategoryRepository.update_restaurant_category(restaurant_category, data)

   return updated_restaurant_category

@restaurant_category_blp.route("/<string:restaurant_category_id>", methods=["DELETE"])
@restaurant_category_blp.response(204)
def delete_restaurant_category(restaurant_category_id):
   restaurant_category = RestaurantCategoryRepository.get_restaurant_category_by_uuid(restaurant_category_id)

   if not restaurant_category:
      abort(404, description="User Not Found")
   RestaurantCategoryRepository.delete_restaurant_category(restaurant_category)
   return ''