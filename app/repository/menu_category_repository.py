from datetime import datetime

from app.extension import db
from app.models.menu_category_model import MenuCategoryModel


class MenuCategoryRepository():

    @staticmethod
    def create_menu_category(data):
        menu_category = MenuCategoryModel(**data)
        db.session.add(menu_category)
        db.session.commit()
        return menu_category

    @staticmethod
    def get_menu_category_by_id(menu_uuid):
        return MenuCategoryModel.query.get(menu_uuid)

    @staticmethod
    def get_menu_category_by_uuid(menu_uuid):
        return MenuCategoryModel.query.filter_by(menu_uuid=menu_uuid).first()

    @staticmethod
    def get_all():
        return MenuCategoryModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_menu_category(menu_category, data):
        for key, value in data.items():
            setattr(menu_category, key, value)
        db.session.commit()
        return menu_category

    @staticmethod
    def delete_menu_category(menu_category):
        menu_category.deleted_at = datetime.utcnow()
        db.session.commit()