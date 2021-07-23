from .db import db


class Kitchen(db.Model):
    __tablename__ = "kitchens"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    kitchen_name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=False)
    service_type_id = db.Column(db.Integer, db.ForeignKey("service_types.id"))

    user = db.relationship("User", back_populates="kitchens")
    service_type = db.relationship(
        "Service_Type", back_populates="service_types")

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user,
            "kitchen_name": self.kitchen_name,
            "active": self.active,
            "service_type": self.service_type
        }
