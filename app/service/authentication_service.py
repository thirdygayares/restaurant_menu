from flask_jwt_extended import create_access_token

from app.repository.authentication_repository import AuthenticationRepository

from app.extension import bcrypt

class AuthenticationService:

    @staticmethod
    def authenticate_user(email, password):
        user = AuthenticationRepository.get_user_by_email(email)

        print(user)

        if not user:
            return None, "Invalid Credentials"

        if not bcrypt.check_password_hash(user.password, password):
            return None, "Invalid Credentials"


        access_token = create_access_token(identity={
            "id": user.user_uuid, "email": user.email
        })

        return{
            "access_token": access_token
        }, None

