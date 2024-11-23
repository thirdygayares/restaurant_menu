from marshmallow import Schema, fields

class LoginSchema(Schema):
    email = fields.Email(required=True, description="User's email address")
    password = fields.Str(required=True, description="User's password", load_only=True)
