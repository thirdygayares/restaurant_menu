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




