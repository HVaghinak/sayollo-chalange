from marshmallow import Schema, fields


class RequestSchema(Schema):
    # TODO Add validation for each of fields when the requirements are clarified

    sdk_version = fields.String(required=True)
    session_id = fields.String(required=True)
    platform = fields.String(required=True)
    username = fields.String(required=True)
    country_code = fields.String(required=True)
