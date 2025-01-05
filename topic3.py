# Stack Node Class
class StackNode:
    def __init__(self, appointment):
        self.appointment = appointment  # Appointment data
        self.next = None  # Reference to the next node in the stack

# Stack Class
class AppointmentStack:
    def __init__(self):
        self.top = None  # Initially, the stack is empty

    def push(self, appointment):
        """Add a new appointment to the top of the stack."""
        new_node = StackNode(appointment)
        if not self.top:
            self.top = new_node  # If the stack is empty, set the first node
        else:
            new_node.next = self.top  # Link the new node to the top
            self.top = new_node  # Update the top of the stack

    def pop(self):
        """Remove and return the most recent appointment (top of the stack)."""
        if not self.top:
            print("Stack is empty. No appointment to pop.")
            return None
        popped_appointment = self.top.appointment
        self.top = self.top.next  # Update the top to the next node
        return popped_appointment

    def peek(self):
        """Return the most recent appointment (top of the stack) without removing it."""
        if not self.top:
            print("Stack is empty. No appointment to peek.")
            return None
        return self.top.appointment

    def display_stack(self):
        """Display all appointments in the stack, from top to bottom."""
        current = self.top
        if not current:
            print("Stack is empty.")
            return
        while current:
            appointment = current.appointment
            print(f"Appointment ID: {appointment['id']}, Name: {appointment['name']}, Service: {appointment['service']}, Time: {appointment['time']}, Priority: {appointment['priority']}")
            current = current.next

# Example usage for Stack
stack = AppointmentStack()

# Add some appointments to the stack
stack.push({"id": 1, "name": "John Doe", "service": "Haircut", "time": "10:00 AM", "priority": 3})
stack.push({"id": 2, "name": "Jane Smith", "service": "Facial", "time": "11:00 AM", "priority": 1})
stack.push({"id": 3, "name": "Emily Davis", "service": "Massage", "time": "2:00 PM", "priority": 5})

# Display the appointments in the stack (top to bottom)
print("Appointments in stack (top to bottom):")
stack.display_stack()

# Peek at the most recent appointment
print("\nPeek at the most recent appointment:")
peeked_appointment = stack.peek()
print(f"Appointment ID: {peeked_appointment['id']}, Name: {peeked_appointment['name']}, Service: {peeked_appointment['service']}, Time: {peeked_appointment['time']}, Priority: {peeked_appointment['priority']}")

# Pop the most recent appointment (removes it from the stack)
popped_appointment = stack.pop()
if popped_appointment:
    print(f"\nPopped Appointment: {popped_appointment}")

# Display the appointments again after popping the most recent one
print("\nAppointments in stack after popping the most recent one:")
stack.display_stack()


