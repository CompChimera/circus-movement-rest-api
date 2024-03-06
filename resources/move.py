from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import MoveModel
from schemas import MoveSchema, MoveUpdateSchema

blp = Blueprint("moves", __name__, description="Operations on moves")

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

        # Try to get an item to update
        # If item not found, create it
        # put requests are expected to operate this way
        if move:
            move.name = move_data["name"]
        else:
            move = MoveModel(id=move_id, **move_data) # make sure to use the ID from the url and not generate one
        # raise NotImplementedError("Deleting an item is not implemented.")
            
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
    
    @blp.arguments(MoveSchema)
    @blp.response(201, MoveSchema)
    def post(self, appr_data):
        move = MoveModel(**appr_data)

        try:
            db.session.add(move)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the move")
        
        return move, 201
    
