from db import db

class MoveModel(db.Model):
    __tablename__ = "moves"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False )
    apparatus_id = db.Column(db.Integer, db.ForeignKey("apparatuses.id"), unique=False, nullable=False)

    apparatus = db.relationship("ApparatusModel", back_populates="moves")
    routine = db.relationship("RoutineModel", back_populates="moves", secondary="routine_moves")
