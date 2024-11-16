from marshmallow import Schema, fields


class RestaurantSchema(Schema):
    restaurant_id = fields.Int(dump_only=True)
    restaurant_uuid = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    phone = fields.Str(required=True)
    email = fields.Email(required=True)
    status = fields.Bool(required=True)
    description = fields.Str(required=True)

    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
