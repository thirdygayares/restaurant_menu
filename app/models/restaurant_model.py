import uuid

from sqlalchemy.dialects.mysql import CHAR

from app.extension import db

class RestaurantModel(db.Model):
    __tablename__ = "restaurant"

    restaurant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_uuid = db.Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)

    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.String(255), nullable=False)

    user_id =  db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('restaurant_category.category_id'), nullable=False)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

