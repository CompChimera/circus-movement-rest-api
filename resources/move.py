from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import MoveModel, ApparatusModel, RoutineModel
from schemas import MoveSchema, MoveUpdateSchema, RoutineAndMoveSchema

blp = Blueprint("moves", __name__, description="Operations on moves")

# Get or Create Apparatus Move
@blp.route("/apparatus/<string:apparatus_id>/move")
class MovesForApparatus(MethodView):
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
        except SQLAlchemyError as e:
            abort(500, message="Error adding move to apparatus")
        
        return move

@blp.route("/routine/<string:routine_id>/move/<string:move_id>")
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

@blp.route("/move/<string:move_id>")
class move(MethodView):
    @blp.response(200, MoveSchema)
    def get(self, move_id):
        move = MoveModel.query.get_or_404(move_id)
        return move
    

    def delete(self, move_id):
        move = MoveModel.query.get_or_404(move_id)
        db.session.delete(move)
        db.session.commit()
        return {"message":"move deleted"}
    
    # TODO: add functionality to update move
    # order is important, we want the response to be deeper set than the arguments
    @blp.arguments(MoveUpdateSchema)
    @blp.response(200, MoveSchema)
    def put(self, move_data, move_id):
        move = MoveModel.query.get(move_id)

        # Try to get an routine to update
        # If routine not found, create it
        # put requests are expected to operate this way
        if move:
            move.name = move_data["name"]
        else:
            move = MoveModel(id=move_id, **move_data) # make sure to use the ID from the url and not generate one
        # raise NotImplementedError("Deleting an routine is not implemented.")
            
        try:
            db.session.add(move)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while saving the move")
        
        return move, 201

@blp.route("/move")
class MoveList(MethodView):
    @blp.response(200, MoveSchema(many=True))
    def get(self):
        return MoveModel.query.all()
    
    # @blp.arguments(MoveSchema)
    # @blp.response(201, MoveSchema)
    # def post(self, appr_data):
    #     move = MoveModel(**appr_data)

    #     try:
    #         db.session.add(move)
    #         db.session.commit()
    #     except SQLAlchemyError:
    #         abort(500, message="An error occured while inserting the move")
        
    #     return move, 201
    
