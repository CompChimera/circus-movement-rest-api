from db import db

class RoutineModel(db.Model):
    __tablename__ = "routines"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False )
    description = db.Column(db.String)
    apparatus_id = db.Column(db.Integer, db.ForeignKey("apparatuses.id"), unique=False, nullable=False)

    apparatus = db.relationship("ApparatusModel", back_populates="routines")
    moves = db.relationship("MoveModel", back_populates="routine", secondary="routine_moves")