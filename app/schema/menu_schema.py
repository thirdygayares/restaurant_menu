from marshmallow import Schema, fields


class MenuSchema(Schema):
    menu_id = fields.Int(dump_only=True)
    menu_uuid = fields.Str(dump_only=True)

    name = fields.Str(required=True)
    price = fields.Int(required=True)
    description = fields.Str(required=True)
    availability = fields.Bool(required=True)

    restaurant_id = fields.Int(required=True)
    category_id = fields.Int(required=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
