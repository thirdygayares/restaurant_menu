from flask_smorest import Blueprint
from flask import abort, jsonify

from app.repository.menu_category_repository import MenuCategoryRepository
from app.schema.menu_category_schema import MenuCategorySchema

menu_category_blp = Blueprint('menu_category','menu_category', url_prefix='/menu-category', description="Operation for Menu Category")


@menu_category_blp.route("/", methods=['POST'])
@menu_category_blp.arguments(MenuCategorySchema)
@menu_category_blp.response(201, MenuCategorySchema)
def create_menu_category(data):
    menu_category = MenuCategoryRepository.create_menu_category(data)
    return menu_category


@menu_category_blp.route("/<string:menu_category_id>", methods=['GET'])
@menu_category_blp.response(200, MenuCategorySchema)
def get_menu_category_by_id(menu_category_id):
   menu_category = MenuCategoryRepository.get_menu_category_by_uuid(menu_category_id)
   if not menu_category:
      return jsonify({"message":"not found"}), 404
   return menu_category

@menu_category_blp.route("/", methods=['GET'])
@menu_category_blp.response(200, MenuCategorySchema(many=True))
def get_all_menu_categorys():
   menu_category = MenuCategoryRepository.get_all()
   return menu_category


@menu_category_blp.route("/<string:menu_category_id>", methods=['PUT'])
@menu_category_blp.arguments(MenuCategorySchema)
@menu_category_blp.response(200, MenuCategorySchema)
def update_menu_category(data, menu_category_id):
   menu_category = MenuCategoryRepository.get_menu_category_by_uuid(menu_category_id)

   if not menu_category:
       abort(404, description="User not found")
   updated_menu_category = MenuCategoryRepository.update_menu_category(menu_category, data)

   return updated_menu_category

@menu_category_blp.route("/<string:menu_category_id>", methods=["DELETE"])
@menu_category_blp.response(204)
def delete_menu_category(menu_category_id):
   menu_category = MenuCategoryRepository.get_menu_category_by_uuid(menu_category_id)

   if not menu_category:
      abort(404, description="User Not Found")
   MenuCategoryRepository.delete_menu_category(menu_category)
   return ''