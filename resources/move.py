from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import MoveModel, ApparatusModel, RoutineModel
from schemas import MoveSchema, MoveUpdateSchema, RoutineAndMoveSchema

blp = Blueprint("moves", __name__, description="Operations on moves")

@blp.route("/apparatus/<int:apparatus_id>/move")
class AddMovesForApparatus(MethodView):
    @blp.response(200, MoveSchema(many=True))
    def get(self, apparatus_id):
        apparatus = ApparatusModel.query.get_or_404(apparatus_id)

        return apparatus.moves.all()

    @blp.arguments(MoveSchema)
    @blp.response(201, MoveSchema)
    def post(self, move_data, apparatus_id):
        #  check if move in store already has this name
        move = MoveModel(**move_data, apparatus_id = apparatus_id)

        try:
            db.session.add(move)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error adding move to apparatus")
        
        return move
    
@blp.route("/apparatus/<int:apparatus_id>/move/<int:move_id>")
class MovesForApparatus(MethodView):
    @blp.response(200, MoveSchema)
    def get(self, move_id, apparatus_id):
        move = MoveModel.query.get_or_404(move_id)
        return move

    def delete(self, apparatus_id, move_id):
        apparatus = ApparatusModel.query.get_or_404(apparatus_id)
        move = MoveModel.query.get_or_404(move_id)

        apparatus.moves.remove(move)

        try:
            db.session.add(apparatus)
            db.session.delete(move)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while removing the move from the apparatus")

        return {"message":"Move removed from Apparatus", "apparatus": apparatus.name}
    
    @blp.arguments(MoveUpdateSchema)
    @blp.response(200, MoveSchema)
    def put(self, move_data, apparatus_id, move_id):
        move = MoveModel.query.get(move_id)

        if move_id:
            move.name = move_data["name"]
        else:
            move = MoveModel(id=move_id, **move_data) 
        raise NotImplementedError("Updating an apparatus move is not yet implemented.")

@blp.route("/routine/<int:routine_id>/move/<int:move_id>")
class LinkMovesToRoutine(MethodView):
    @blp.response(200, RoutineAndMoveSchema)
    def post(self, routine_id, move_id):
        routine = RoutineModel.query.get_or_404(routine_id)
        move = MoveModel.query.get_or_404(move_id)

        try:
            routine.moves.append(move)
            db.session.add(routine)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the move to the routine.")
        
        return {"message":"Move added to routine", "routine": routine, "move": move}

    @blp.response(200, RoutineAndMoveSchema)
    def delete(self, routine_id, move_id):
        routine = RoutineModel.query.get_or_404(routine_id)
        move = MoveModel.query.get_or_404(move_id)

        routine.moves.remove(move)

        try:
            db.session.add(routine)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the move")
        
        return {"message":"routine removed from move", "routine": routine, "move":move}

@blp.route("/move/<int:move_id>")
class move(MethodView):
    @blp.response(200, MoveSchema)
    def get(self, move_id):
        move = MoveModel.query.get_or_404(move_id)
        return move

@blp.route("/move")
class MoveList(MethodView):
    @blp.response(200, MoveSchema(many=True))
    def get(self):
        return MoveModel.query.all()
