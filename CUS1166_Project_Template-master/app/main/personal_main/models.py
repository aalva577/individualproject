# an appointment title, an appointment date, starting time, an duration,
# the location the appointment will take place (customer's address), the customer's name, and notes.
from app import db




class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    address = db.Column(db.String(128), index=True)


class Appointment(db.model):
    id = db.Column(db.Integer, primary_key=True)
    app_title = db.Column(db.String(128), nullable=False)
    app_date = db.Column(db.String(128), nullable=False)
    start_time = db.Column(CharField(max_length=5), nullable=False)
    duration = db.Column(db.String(128), nullable=False)
    app_location = db.Column(db.String(128), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customer.id') nullable=False)
    app_notes = db.Column(db.String(128), nullable=True)
    app_status = db.Column(db.String(128), nullable=True)
