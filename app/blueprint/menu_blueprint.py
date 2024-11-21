from flask_smorest import Blueprint
from flask import abort, jsonify

from app.repository.menu_repository import MenuRepository
from app.schema.menu_schema import MenuSchema

menu_blp = Blueprint('menu','menu', url_prefix='/menu', description="Operation for Menu Category")


@menu_blp.route("/", methods=['POST'])
@menu_blp.arguments(MenuSchema)
@menu_blp.response(201, MenuSchema)
def create_menu(data):
    menu = MenuRepository.create_menu(data)
    return menu


@menu_blp.route("/<string:menu_id>", methods=['GET'])
@menu_blp.response(200, MenuSchema)
def get_menu_by_id(menu_id):
   menu = MenuRepository.get_menu_by_uuid(menu_id)
   if not menu:
      return jsonify({"message":"not found"}), 404
   return menu

@menu_blp.route("/", methods=['GET'])
@menu_blp.response(200, MenuSchema(many=True))
def get_all_menus():
   menu = MenuRepository.get_all()
   return menu

@menu_blp.route("/restaurant/<string:restaurant_uuid>", methods=['GET'])
@menu_blp.response(200, MenuSchema(many=True))
def get_menu_by_restaurant(restaurant_uuid):
   menu = MenuRepository.get_all_by_restaurant(restaurant_uuid)
   if not menu:
      return jsonify({"message":" restaurant not found"}), 404
   print("menu is")
   print(menu)
   return menu


@menu_blp.route("/<string:menu_id>", methods=['PUT'])
@menu_blp.arguments(MenuSchema)
@menu_blp.response(200, MenuSchema)
def update_menu(data, menu_id):
   menu = MenuRepository.get_menu_by_uuid(menu_id)

   if not menu:
       abort(404, description="User not found")
   updated_menu = MenuRepository.update_menu(menu, data)

   return updated_menu

@menu_blp.route("/<string:menu_id>", methods=["DELETE"])
@menu_blp.response(204)
def delete_menu(menu_id):
   menu = MenuRepository.get_menu_by_uuid(menu_id)

   if not menu:
      abort(404, description="User Not Found")
   MenuRepository.delete_menu(menu)
   return ''