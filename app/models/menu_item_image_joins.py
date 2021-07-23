from .db import db


class Menu_Item_Image_Join(db.Model):
    __tablename__ = "menu_item_image_joins"

    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey("images.id"))
    menu_item_id = db.Column(db.Integer, db.ForeignKey("menu_items.id"))

    image = db.relationship("Image", back_populates="menu_item_image_joins")
    menu_item = db.relationship(
        "Menu_Item", back_populates="menu_item_image_joins")

    def to_dict(self):
        return{
            "id": self.id,
            "image": self.image,
            "menu_item": self.menu_item
        }
