from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(dump_only=True)     # dump_only는 DB에서 해당 데이터를 관리한다는 함수이다.
    title = fields.String(required=True)
    author = fields.String(required=True)