from marshmallow import Schema, fields


class MenuCategorySchema(Schema):
    menu_id = fields.Int(dump_only=True)
    menu_uuid = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)