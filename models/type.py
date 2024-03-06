# from db import db

# class TypeModel(db.Model):
#     __tablename__ = "types"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False )

    # TODO: Maybe actually wait to do this one, and flesh out the Move and Routine to connect to a apparatus. And we can name the Apparatus to signify different types
    # EX. 'Single Point Hoop', 'Double Point Hoop', 'Doubles Hoop'

    # apparatus id
    # apparatus_id = db.Column(db.Integer, db.ForeignKey("apparatuses.id"), unique=False, nullable=False)

    # relationship to apparatus
    # apparatus = db.relationship("ApparatusModel", back_populates="apparatuses")