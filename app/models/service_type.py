from .db import db


class Service_Type(db.Model):
    __tablename__ = "service_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    service_speed = db.Column(db.Integer, nullable=False)

    kitchens = db.relationship(
        "Kitchen", back_populates="service_type")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "service_speed": self.service_speed
        }
