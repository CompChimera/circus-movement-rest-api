import os

from flask import Flask
from flask_smorest import Api

from db import db

import models

from resources.apparatus import blp as ApparatusBlueprint
from resources.routine import blp as RoutineBlueprint
from resources.move import blp as MoveBlueprint
# from resources.type import blp as TypeBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app) # connect app to sqlalchemy

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ApparatusBlueprint)
    api.register_blueprint(RoutineBlueprint)
    # api.register_blueprint(TypeBlueprint)
    api.register_blueprint(MoveBlueprint)

    return app