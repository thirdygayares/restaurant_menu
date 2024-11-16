from app.extension import db
from app.models.menu_model import MenuModel


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
        return MenuModel.query.filter_by(menu_uuid=menu_uuid).first()

    @staticmethod
    def get_all():
        return MenuModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_menu(menu, data):
        for key, value in data.items():
            setattr(menu, key, value)
        db.session.commit()
        return menu

    @staticmethod
    def delete_menu(menu):
        menu.deleted_at = MenuModel.utcnow()
        db.session.commit()