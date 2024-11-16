from datetime import datetime

from sqlalchemy import delete

from app.extension import db
from app.models.user_model import UserModel

class UserRepository:

    @staticmethod
    def create_user(data):
        user = UserModel(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return UserModel.query.get(user_id)

    @staticmethod
    def get_user_by_uuid(user_uuid):
        return UserModel.query.filter_by(user_uuid=user_uuid).first()

    @staticmethod
    def get_all():
        return UserModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_user(user, data):
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user):
        user.deleted_at = datetime.utcnow()
        db.session.commit()





