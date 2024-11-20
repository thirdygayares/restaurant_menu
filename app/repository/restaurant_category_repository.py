from datetime import datetime

from app.extension import db
from app.models.restaurant_category_model import RestaurantCategoryModel


class RestaurantCategoryRepository():

    @staticmethod
    def create_restaurant_category(data):
        restaurant = RestaurantCategoryModel(**data)
        db.session.add(restaurant)
        db.session.commit()
        return restaurant

    @staticmethod
    def get_restaurant_category_by_id(category_id):
        return RestaurantCategoryModel.query.get(category_id)

    @staticmethod
    def get_restaurant_category_by_uuid(category_uuid):
        return RestaurantCategoryModel.query.filter_by(category_uuid=category_uuid).first()

    @staticmethod
    def get_all():
        return RestaurantCategoryModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_restaurant_category(restaurant, data):
        for key, value in data.items():
            setattr(restaurant, key, value)
        db.session.commit()
        return restaurant

    @staticmethod
    def delete_restaurant_category(restaurant):
        restaurant.deleted_at = datetime.utcnow()
        db.session.commit()