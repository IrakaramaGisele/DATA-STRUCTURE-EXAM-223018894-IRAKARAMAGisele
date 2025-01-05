# Linked List Node class to store appointment data
class AppointmentNode:
    def __init__(self, appointment):
        self.appointment = appointment  # Appointment data
        self.next = None  # Reference to the next node in the list

# Linked List class for managing appointments
class AppointmentLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def add_appointment(self, appointment):
        """Add a new appointment to the end of the linked list."""
        new_node = AppointmentNode(appointment)
        if not self.head:
            self.head = new_node  # If list is empty, the new node becomes the head
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Add the new node at the end of the list

    def remove_appointment(self, appointment_id):
        """Remove an appointment by its ID."""
        if not self.head:
            print("The list is empty. No appointment to remove.")
            return

        # If the appointment to be removed is at the head
        if self.head.appointment["id"] == appointment_id:
            self.head = self.head.next
            print(f"Appointment ID {appointment_id} removed.")
            return

        # Traverse the list to find the appointment to remove
        current = self.head
        while current.next and current.next.appointment["id"] != appointment_id:
            current = current.next

        if current.next:  # Appointment found
            current.next = current.next.next
            print(f"Appointment ID {appointment_id} removed.")
        else:
            print(f"Appointment ID {appointment_id} not found.")

    def display_appointments(self):
        """Display all appointments in the list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        print("Appointments in the list:")
        while current:
            appointment = current.appointment
            print(f"Appointment ID: {appointment['id']}, Name: {appointment['name']}, Service: {appointment['service']}, Time: {appointment['time']}, Priority: {appointment['priority']}")
            current = current.next

    def peek_first(self):
        """Return the first appointment (head) without removing it."""
        if self.head:
            return self.head.appointment
        print("The list is empty.")
        return None

    def peek_last(self):
        """Return the last appointment (tail) without removing it."""
        if not self.head:
            print("The list is empty.")
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.appointment

# Example usage for Linked List
linked_list = AppointmentLinkedList()

# Add some appointments to the linked list
linked_list.add_appointment({"id": 1, "name": "John Doe", "service": "Haircut", "time": "10:00 AM", "priority": 3})
linked_list.add_appointment({"id": 2, "name": "Jane Smith", "service": "Facial", "time": "11:00 AM", "priority": 1})
linked_list.add_appointment({"id": 3, "name": "Emily Davis", "service": "Massage", "time": "2:00 PM", "priority": 5})

# Display all appointments in the linked list
linked_list.display_appointments()

# Peek at the first and last appointment
first_appointment = linked_list.peek_first()
last_appointment = linked_list.peek_last()

print("\nPeek at the first appointment:")
if first_appointment:
    print(f"Appointment ID: {first_appointment['id']}, Name: {first_appointment['name']}")

print("\nPeek at the last appointment:")
if last_appointment:
    print(f"Appointment ID: {last_appointment['id']}, Name: {last_appointment['name']}")

# Remove an appointment by its ID
linked_list.remove_appointment(2)

# Display all appointments after removing one
linked_list.display_appointments()

# Try removing an appointment that doesn't exist
linked_list.remove_appointment(4)

# Display the appointments after an unsuccessful removal
linked_list.display_appointments()

