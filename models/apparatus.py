from db import db

class ApparatusModel(db.Model):
    __tablename__ = "apparatuses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False )

    # For later:
    # type_id = db.Column(db.Integer, db.ForeignKey("types.id"),  unique=False, nullable=False)
    
    # when we have a key that's connected to the moves table, we can map to that table
    # Because the TypeModel says it's connected to the types table
    #  back_populates means that type.py will have an types relationship
    # types = db.relationship("TypeModel", back_populates="types")
    
    routines = db.relationship("RoutineModel", back_populates="apparatus")


    # Duplicate for Moves - need to double check the one - many, many - many config requirements
    moves = db.relationship("MoveModel", back_populates="apparatus",  lazy="dynamic", cascade="all, delete")