from marshmallow import Schema, fields, validate

class RegisterSchemaByEmailPasswordSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, validate=validate.Length(min=1))
    firstName = fields.Str(required=True, validate=validate.Length(min=1))
    lastName = fields.Str(required=True, validate=validate.Length(min=1))
    phone = fields.Str(required=True, validate=validate.Length(min=1))
    