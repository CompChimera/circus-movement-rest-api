from marshmallow import Schema, fields

class PlainApparatusSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainMoveSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainRoutineSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class ApparatusSchema(PlainApparatusSchema):  
    routines = fields.List(fields.Nested(PlainRoutineSchema()), dump_only=True)
    moves = fields.List(fields.Nested(PlainMoveSchema), dump_only=True)
    # type 

class ApparatusUpdateSchema(Schema):
    name = fields.Str()

class RoutineSchema(PlainRoutineSchema):
    apparatus_id = fields.Int(load_only=True)
    apparatus = fields.Nested(PlainApparatusSchema(), dump_only=True)
    moves = fields.List(fields.Nested(PlainMoveSchema()), dump_only=True)

class RoutineUpdateSchema(Schema):
    name = fields.Str()
    moves = fields.List(fields.Nested(PlainMoveSchema()), dump_only=True)

class MoveSchema(PlainMoveSchema):
    apparatus_id = fields.Int(load_only=True)
    apparatus = fields.Nested(PlainApparatusSchema(), dump_only=True)
    routine = fields.List(fields.Nested(PlainRoutineSchema), dump_only=True)

class MoveUpdateSchema(Schema):
    name = fields.Str()

class RoutineAndMoveSchema(Schema):
    routine = fields.Nested(RoutineSchema)
    message = fields.Str(),
    move = fields.Nested(MoveSchema)

# TODO: Types
##class PlainTypeSchema(Schema):
# class TypeSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str(required=True)
# class TypeSchema(PlainTypeSchema):

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(require=True)
    password = fields.Str(require=True, load_only=True)
