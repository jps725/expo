from .db import db


class Menu_Item(db.Model):
    __tablename__ = "menu_items"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255), nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey(
        "stations.id"), nullable=False)
    fire_time_seconds = db.Column(db.Integer, nullabe=False)
    active = db.Column(db.Boolean, default=False)

    station = db.relationship("Station", back_populates="menu_items")

    def to_dict(self):
        return{
            "id": self.id,
            "item_name": self.item_name,
            "station": self.station,
            "fire_time_seconds": self.fire_time_seconds,
            "active": self.active
        }
