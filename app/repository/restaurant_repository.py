from app.extension import db
from app.models.restaurant_model import RestaurantModel


class RestaurantRepository():

    @staticmethod
    def create_restaurant(data):
        restaurant = RestaurantModel(**data)
        db.session.add(restaurant)
        db.session.commit()
        return restaurant

    @staticmethod
    def get_restaurant_by_id(category_uuid):
        return RestaurantModel.query.get(category_uuid)

    @staticmethod
    def get_restaurant_by_uuid(category_uuid):
        return RestaurantModel.query.filter_by(category_uuid=category_uuid).first()

    @staticmethod
    def get_all():
        return RestaurantModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_restaurant(restaurant, data):
        for key, value in data.items():
            setattr(restaurant, key, value)
        db.session.commit()
        return restaurant

    @staticmethod
    def delete_restaurant(restaurant):
        restaurant.deleted_at = RestaurantModel.utcnow()
        db.session.commit()