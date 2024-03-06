from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ApparatusModel
from schemas import ApparatusSchema, ApparatusUpdateSchema

blp = Blueprint("Apparatuses", __name__, description="Operations on apparatuses")

@blp.route("/apparatus/<string:appr_id>")
class apparatus(MethodView):
    @blp.response(200, ApparatusSchema)
    def get(self, appr_id):
        apparatus = ApparatusModel.query.get_or_404(appr_id)
        return apparatus
    
    def delete(self, appr_id):
        apparatus = ApparatusModel.query.get_or_404(appr_id)
        db.session.delete(apparatus)
        db.session.commit()
        return {"message":"apparatus deleted"}
    
    # TODO: add functionality to update apparatus
    @blp.arguments(ApparatusUpdateSchema)
    @blp.response(200, ApparatusSchema)
    def put(self, appr_data, appr_id):
        apparatus = ApparatusModel.query.get(appr_id)
        # Try to get an item to update
        # If item not found, create it

        # if item:
        #     item.price = appr_data["price"]
        #     item.name = appr_data["name"]
        # else:
        #     item = ApparatusModel(id=appr_id, **appr_data) # make sure to use the ID from the url and not generate one
        raise NotImplementedError("Updating an apparatus is not implemented yet.")

@blp.route("/apparatus")
class ApparatusList(MethodView):
    @blp.response(200, ApparatusSchema(many=True))
    def get(self):
        return ApparatusModel.query.all()
    
    @blp.arguments(ApparatusSchema)
    @blp.response(201, ApparatusSchema)
    def post(self, appr_data):
        apparatus = ApparatusModel(**appr_data)

        try:
            db.session.add(apparatus)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the apparatus")
        
        return apparatus, 201
    
