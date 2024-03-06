from db import db

class RoutineModel(db.Model):
    __tablename__ = "routines"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False )


    # apparatus id
    apparatus_id = db.Column(db.Integer, db.ForeignKey("apparatuses.id"), unique=False, nullable=False)

    # relationship to apparatus
    apparatus = db.relationship("ApparatusModel", back_populates="routines")

    # relationship to moves - list where order in important. Similar to items <> tags?
    # moves = db.relationship("MoveModel", back_populates="moves", secondary="routine_moves")