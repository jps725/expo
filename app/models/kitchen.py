from .db import db


class Kitchen(db.Model):
    __tablename__ = "kitchens"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    kitchen_name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=False)
