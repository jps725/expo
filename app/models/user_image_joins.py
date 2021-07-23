from .db import db


class User_Image_Join(db.Model):
    __tablename__ = "user_image_joins"

    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey("images.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    image = db.relationship("Image", back_populates="user_image_joins")
    user = db.relationship(
        "User", back_populates="user_image_joins")

    def to_dict(self):
        return{
            "id": self.id,
            "image": self.image,
            "user": self.user
        }
