from .db import db
from datetime import datetime, timezone


class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    kitchen_id = db.Column(db.Integer, db.ForeignKey(
        "kitchens.id"), nullable=False)
    table_number = db.Column(db.Integer, nullable=False)
    server_name = db.Column(db.String(100), nullable=False)
    start_time = db.Column(
        db.TimeStamp(), default=datetime.now(timezone.utc), nullable=False)
    end_time = db.Column(db.TimeStamp())
    send_time = db.Column(db.TimeStamp())
    active = db.Column(db.Boolean, default=True)

    kitchen = db.relationship("Kitchen", back_populates="tickets")

    def to_dict(self):
        return {
            "id": self.id,
            "kitchen": self.kitchen,
            "table_number": self.table_number,
            "server_name": self.server_name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "send_time": self.send_time,
            "active": self.active
        }
