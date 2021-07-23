from .db import db


class Station_Image_Join(db.Model):
    __tablename__ = "station_image_joins"

    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey("images.id"))
    station_id = db.Column(db.Integer, db.ForeignKey("stations.id"))

    image = db.relationship("Image", back_populates="station_image_joins")
    station = db.relationship("Station", back_populates="station_image_joins")

    def to_dict(self):
        return{
            "id": self.id,
            "image": self.image,
            "station": self.station
        }
