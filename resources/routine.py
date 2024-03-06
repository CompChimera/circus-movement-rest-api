from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import RoutineModel
from schemas import RoutineSchema, RoutineUpdateSchema

blp = Blueprint("routines", __name__, description="Operations on routines")

@blp.route("/routine/<string:routine_id>")
class routine(MethodView):
    @blp.response(200, RoutineSchema)
    def get(self, routine_id):
        routine = RoutineModel.query.get_or_404(routine_id)
        return routine
    

    def delete(self, routine_id):
        routine = RoutineModel.query.get_or_404(routine_id)
        db.session.delete(routine)
        db.session.commit()
        return {"message":"routine deleted"}
    
    @blp.arguments(RoutineUpdateSchema)
    @blp.response(200, RoutineSchema)
    def put(self, routine_data, routine_id):
        routine = RoutineModel.query.get(routine_id)

        if routine:
            routine.name = routine_data["name"]
        else:
            routine = RoutineModel(id=routine_id, **routine_data) 
            
        try:
            db.session.add(routine)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while saving the routine")
        
        return routine, 201

@blp.route("/routine")
class RoutineList(MethodView):
    @blp.response(200, RoutineSchema(many=True))
    def get(self):
        return RoutineModel.query.all()
    
    @blp.arguments(RoutineSchema)
    @blp.response(201, RoutineSchema)
    def post(self, appr_data):
        routine = RoutineModel(**appr_data)

        try:
            db.session.add(routine)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the routine")
        
        return routine, 201
    
