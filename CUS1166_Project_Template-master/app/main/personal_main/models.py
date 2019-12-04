# an appointment title, an appointment date, starting time, an duration,
# the location the appointment will take place (customer's address), the customer's name, and notes.
from app import db


class Appointment(db.model):
    __tablename__ = "Appointments"
    id = db.Column(db.Integer, primary_key=True)

    app_title = db.Column(db.String, nullable=False)
    app_date = db.Column(db.String, nullable=False)
    start_time = db.Column(CharField(max_length=5), nullable=False)
    duration = db.Column(db.String, nullable=False)
    app_location = db.Column(db.String, nullable=False)
    customer_name = db.Column(db.String, nullable=False)
    app_notes = db.Column(db.String, nullable=True)
