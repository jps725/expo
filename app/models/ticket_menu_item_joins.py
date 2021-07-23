from .db import db
from datetime import datetime


class Ticket_Menu_Item_Join(db.Model):
    __tablename__ = "ticket_menu_item_joins"

    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey("tickets.id"))
    menu_item_id = db.Column(db.Integer, db.ForeignKey("menu_items.id"))
    start_time = db.Column(db.TimeStamp)
    end_time = db.Column(db.TimeStamp)
    complete = db.Column(db.Boolean, default=False)

    ticket = db.relationship("Ticket", back_populates="ticket_menu_item_joins")
    menu_item = db.relationship(
        "Menu_Item", back_populates="ticket_menu_joins")

    def to_dict(self):
        return {
            "id": self.id,
            "ticket": self.ticket,
            "menu_item": self.menu_item,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "complete": self.complete
        }
