from .db import db


class Kitchen_Image_Join(db.Model):
    __tablename__ = "kitchen_image_joins"

    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey("images.id"))
    kitchen_id = db.Column(db.Integer, db.ForeignKey("kitchens.id"))

    image = db.relationship("Image", back_populates="kitchen_image_joins")
    kitchen = db.relationship(
        "Kitchen", back_populates="kitchen_image_joins")

    def to_dict(self):
        return{
            "id": self.id,
            "image": self.image,
            "kitchen": self.kitchen
        }
