from db import db


class RoutineMoves(db.Model):
    __tablename__ = "routine_moves"

    id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.Integer, db.ForeignKey("routines.id"))
    move_id = db.Column(db.Integer, db.ForeignKey("moves.id"))