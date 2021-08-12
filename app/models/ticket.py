from .db import db
from sqlalchemy.sql import func


class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    kitchen_id = db.Column(db.Integer, db.ForeignKey(
        "kitchens.id"), nullable=False)
    table_number = db.Column(db.Integer, nullable=False)
    server_name = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(), nullable=False)
    end_time = db.Column(db.DateTime(timezone=True))
    send_time = db.Column(db.DateTime(timezone=True))
    active = db.Column(db.Boolean, default=True)

    kitchen = db.relationship("Kitchen", back_populates="tickets")
    ticket_menu_item_joins = db.relationship(
        "Ticket_Menu_Item_Join", back_populates="ticket")

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
