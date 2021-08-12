from .db import db


class Station(db.Model):
    __tablename__ = "stations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    kitchen_id = db.Column(db.Integer, db.ForeignKey(
        "kitchens.id"), nullable=False)
    active = db.Column(db.Boolean, default=False)

    kitchen = db.relationship("Kitchen", back_populates="stations")
    menu_items = db.relationship("Menu_Item", back_populates="station")
    station_image_joins = db.relationship(
        "Station_Image_Join", back_populates="station")

    def to_dict():
        return{
            "id": self.id,
            "name": self.name,
            "kitchen": self.kitchen,
            "active": self.active
        }
