from marshmallow import Schema, fields

# Iteration one will be adding, updating, and removing all these all separate entries
#  TODO: connect the pieces together

# class PlainApparatusSchema(Schema):
class ApparatusSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

# class PlainTypeSchema(Schema):
class TypeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

# Should work similarly to item and store in course code
# class PlainMoveSchema(Schema):
class MoveSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

# class ApparatusSchema(PlainApparatusSchema):    
    # type 
    # moves

# class TypeSchema(PlainTypeSchema):
    # relationship to apparatus

# class MoveSchema(PlainMoveSchema)
    # apparatus
    