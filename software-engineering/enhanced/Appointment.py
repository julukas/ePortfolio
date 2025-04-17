from datetime import datetime

"""Initializes Appointment class with some basic input validation, with explanations if rejected"""
class Appointment:
    def __init__(self, appointment_id, appointment_date, patient_name, doctor_name, appointment_type, notes=""):
        if not appointment_id or len(appointment_id) > 10:
            raise ValueError("Invalid appointment ID (must be <= 10 characters).")
        """verify to see if appointment_date is same type as datetime"""
        if not isinstance(appointment_date, datetime) or appointment_date < datetime.now():
            raise ValueError("Invalid appointment date (cannot be in the past).")
        if not patient_name or len(patient_name) > 50:
            raise ValueError("Invalid patient name (must be <= 50 characters).")
        if not doctor_name or len(doctor_name) > 50:
            raise ValueError("Invalid doctor name (must be <= 50 characters).")
        if not appointment_type or len(appointment_type) > 30:
            raise ValueError("Invalid appointment type (must be <= 30 characters).")
        if len(notes) > 200:
            raise ValueError("Notes must be <= 200 characters.")

        self.appointment_id = appointment_id
        self.appointment_date = appointment_date
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_type = appointment_type
        self.notes = notes

    """updates appointment time"""
    def update_appointment_date(self, new_date):
        if not isinstance(new_date, datetime) or new_date < datetime.now():
            raise ValueError("New appointment date must be in the future.")
        self.appointment_date = new_date

    """updates notes"""
    def update_notes(self, new_notes):
        if len(new_notes) > 200:
            raise ValueError("Notes must be <= 200 characters.")
        self.notes = new_notes

    """returns appointment details as a JSON object for API use"""
    def to_json(self):
        return {
            "appointment_id": self.appointment_id,
            "appointment_date": self.appointment_date.strftime("%Y-%m-%d %H:%M"),
            "patient_name": self.patient_name,
            "doctor_name": self.doctor_name,
            "appointment_type": self.appointment_type,
            "notes": self.notes
        }