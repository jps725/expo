from .db import db


class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))

    user_image_joins = db.relationship(
        "User_Image_Join", back_populates="image")
    kitchen_image_joins = db.relationship(
        "Kitchen_Image_Join", back_populates="image")
    menu_item_image_joins = db.relationship(
        "Menu_Item_Image_Join", back_populates="image")
    station_image_joins = db.relationship(
        "Station_Image_Join", back_populates="image")

    def to_dict(self):
        return{
            "id": self.id,
            "image_url": self.image_url
        }
