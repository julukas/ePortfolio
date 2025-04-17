import unittest
from datetime import datetime, timedelta
from Appointment import Appointment

class TestAppointment(unittest.TestCase):
    def setUp(self):
        """runs before each test to set up test cases, sets it 2 days in future"""
        self.valid_date = datetime.now() + timedelta(days=2)
        self.appt = Appointment("A86753", self.valid_date, "Julius Lukas", "Dr. Walker", "Check-up")

    def test_valid_appointment_creation(self):
        """Tests creating a valid appointment"""
        self.assertEqual(self.appt.appointment_id, "A86753")
        self.assertEqual(self.appt.patient_name, "Julius Lukas")
        self.assertEqual(self.appt.doctor_name, "Dr. Walker")
        self.assertEqual(self.appt.appointment_type, "Check-up")
        self.assertEqual(self.appt.appointment_date, self.valid_date)

    def test_all_invalid_inputs(self):
        """tests that when each value is wrong then it raises an error."""
        past_date = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValueError):
            Appointment("B1111", past_date, "Luke Lukas", "Dr. Runner", "Consultation")

    def test_invalid_past_date(self):
        """tests that when only date value is wrong then it raises an error."""
        past_date = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValueError):
            Appointment("A86753", past_date, "Julius Lukas", "Dr. Walker", "Check-up")

    def test_update_appointment_date(self):
        """test to update the appointment date."""
        new_date = datetime.now() + timedelta(days=5)
        self.appt.update_appointment_date(new_date)
        self.assertEqual(self.appt.appointment_date, new_date)

    def test_invalid_update_date(self):
        """updating to a past date raises an error"""
        past_date = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValueError):
            self.appt.update_appointment_date(past_date)

    def test_update_notes(self):
        """test updating notes"""
        self.appt.update_notes("Lisinopril dose increased")
        self.assertEqual(self.appt.notes, "Lisinopril dose increased")

    def test_invalid_notes_length(self):
        """test for excessively long note"""
        long_notes = "c" * 201  #string that is 201 characters long
        with self.assertRaises(ValueError):
            self.appt.update_notes(long_notes)

if __name__ == '__main__':
    unittest.main()
