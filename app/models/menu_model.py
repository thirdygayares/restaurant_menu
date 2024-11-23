import uuid

from sqlalchemy.dialects.mysql import CHAR

from app.extension import db


class MenuModel(db.Model):
    __tablename__ = "menu"

    menu_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_uuid = db.Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)

    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    availability = db.Column(db.Boolean, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.restaurant_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('menu_category.menu_id'), nullable=False)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)