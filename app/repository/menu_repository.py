from datetime import datetime

from app.extension import db
from app.models.menu_model import MenuModel
from app.models.restaurant_model import RestaurantModel


class MenuRepository():

    @staticmethod
    def create_menu(data):
        menu = MenuModel(**data)
        db.session.add(menu)
        db.session.commit()
        return menu

    @staticmethod
    def get_menu_by_id(menu_uuid):
        return MenuModel.query.get(menu_uuid)

    @staticmethod
    def get_menu_by_uuid(menu_uuid):
        return MenuModel.query.filter_by(menu_uuid=menu_uuid, deleted_at=None).first()

    @staticmethod
    def get_all():
        return MenuModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def get_all_by_restaurant(restaurant_uuid):
        restaurant = RestaurantModel.query.filter_by(restaurant_uuid=restaurant_uuid).first()
        if not restaurant:
            return []

        restaurant_id = restaurant.restaurant_id
        print(restaurant_id)
        return MenuModel.query.filter_by(restaurant_id=restaurant_id, deleted_at=None).all()

    @staticmethod
    def update_menu(menu, data):
        for key, value in data.items():
            setattr(menu, key, value)
        db.session.commit()
        return menu

    @staticmethod
    def delete_menu(menu):
        menu.deleted_at = datetime.utcnow()
        db.session.commit()