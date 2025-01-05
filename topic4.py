from collections import deque

class AppointmentDeque:
    def __init__(self, max_size):
        self.max_size = max_size  # Maximum size of the deque
        self.appointment_deque = deque()  # Create an empty deque to store appointments

    def add_appointment(self, appointment):
        """Add a new appointment to the deque."""
        if len(self.appointment_deque) == self.max_size:
            # If deque is full, remove the oldest appointment (from the front)
            self.appointment_deque.popleft()
        self.appointment_deque.append(appointment)  # Add the new appointment to the back

    def remove_appointment(self):
        """Remove the most recent appointment (from the back)."""
        if not self.appointment_deque:
            print("Deque is empty. No appointment to remove.")
            return None
        return self.appointment_deque.pop()

    def display_appointments(self):
        """Display all appointments in the deque from front to back."""
        if not self.appointment_deque:
            print("Deque is empty.")
            return
        print("Appointments in Deque (front to back):")
        for appointment in self.appointment_deque:
            print(f"Appointment ID: {appointment['id']}, Name: {appointment['name']}, Service: {appointment['service']}, Time: {appointment['time']}, Priority: {appointment['priority']}")

    def peek_front(self):
        """Return the first appointment in the deque (front) without removing it."""
        if not self.appointment_deque:
            print("Deque is empty. No appointment to peek.")
            return None
        return self.appointment_deque[0]

    def peek_back(self):
        """Return the last appointment in the deque (back) without removing it."""
        if not self.appointment_deque:
            print("Deque is empty. No appointment to peek.")
            return None
        return self.appointment_deque[-1]

# Example usage for Deque
appointment_deque = AppointmentDeque(max_size=3)  # Maximum size of deque is 3

# Add some appointments to the deque
appointment_deque.add_appointment({"id": 1, "name": "John Doe", "service": "Haircut", "time": "10:00 AM", "priority": 3})
appointment_deque.add_appointment({"id": 2, "name": "Jane Smith", "service": "Facial", "time": "11:00 AM", "priority": 1})
appointment_deque.add_appointment({"id": 3, "name": "Emily Davis", "service": "Massage", "time": "2:00 PM", "priority": 5})

# Display all appointments in the deque
appointment_deque.display_appointments()

# Add another appointment, which will remove the oldest one (since the deque size is 3)
appointment_deque.add_appointment({"id": 4, "name": "Michael Brown", "service": "Manicure", "time": "3:00 PM", "priority": 2})

# Display all appointments after adding a new one (oldest should be removed)
appointment_deque.display_appointments()

# Peek at the front and back appointments
front_appointment = appointment_deque.peek_front()
back_appointment = appointment_deque.peek_back()

print("\nPeek at the front appointment:")
if front_appointment:
    print(f"Appointment ID: {front_appointment['id']}, Name: {front_appointment['name']}")

print("\nPeek at the back appointment:")
if back_appointment:
    print(f"Appointment ID: {back_appointment['id']}, Name: {back_appointment['name']}")

# Remove the most recent appointment (from the back)
removed_appointment = appointment_deque.remove_appointment()
if removed_appointment:
    print(f"\nRemoved Appointment: {removed_appointment}")

# Display all appointments after removing the most recent one
appointment_deque.display_appointments()



