from db import db

class ApparatusModel(db.Model):
    __tablename__ = "apparatuses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    routines = db.relationship("RoutineModel", back_populates="apparatus")
    moves = db.relationship("MoveModel", back_populates="apparatus",  lazy="dynamic", cascade="all, delete")

    # TODO: type
    # type_id = db.Column(db.Integer, db.ForeignKey("types.id"),  unique=False, nullable=False)
    
    # types = db.relationship("TypeModel", back_populates="types")
    
