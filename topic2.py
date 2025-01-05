# Singly Linked List Node Class
class AppointmentNode:
    def __init__(self, appointment):
        self.appointment = appointment  # Appointment data (appointment details)
        self.next = None  # Reference to the next node in the list

# Singly Linked List Class
class AppointmentLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def add_appointment(self, appointment):
        """Add a new appointment to the end of the list."""
        new_node = AppointmentNode(appointment)
        if not self.head:
            self.head = new_node  # If list is empty, set the first node
        else:
            current = self.head
            while current.next:
                current = current.next  # Traverse to the end of the list
            current.next = new_node  # Add the new node to the end

    def display_appointments(self):
        """Display all appointments in the list."""
        current = self.head
        while current:
            appointment = current.appointment
            print(f"Appointment ID: {appointment['id']}, Name: {appointment['name']}, Service: {appointment['service']}, Time: {appointment['time']}, Priority: {appointment['priority']}")
            current = current.next

    def find_appointment(self, appointment_id):
        """Find an appointment by ID."""
        current = self.head
        while current:
            if current.appointment['id'] == appointment_id:
                return current.appointment
            current = current.next
        return None  # Return None if the appointment is not found

# singly linked list implementation
linked_list = AppointmentLinkedList()

# Add some appointments
linked_list.add_appointment({"id": 1, "name": "John Doe", "service": "Haircut", "time": "10:00 AM", "priority": 3})
linked_list.add_appointment({"id": 2, "name": "Jane Smith", "service": "Facial", "time": "11:00 AM", "priority": 1})
linked_list.add_appointment({"id": 3, "name": "Emily Davis", "service": "Massage", "time": "2:00 PM", "priority": 5})

# Display all appointments
linked_list.display_appointments()

# Find a specific appointment by ID
appointment = linked_list.find_appointment(2)
if appointment:
    print(f"\nFound Appointment: {appointment}")
else:
    print("\nAppointment not found.")
    # Binary Search Tree Node Class
class BSTNode:
    def __init__(self, appointment):
        self.appointment = appointment  # Appointment data (appointment details)
        self.left = None  # Left child (lower priority)
        self.right = None  # Right child (higher priority)

# Binary Search Tree (BST) Class
class AppointmentBST:
    def __init__(self):
        self.root = None  # Initially, the BST is empty

    def insert(self, appointment):
        """Insert a new appointment into the BST based on priority."""
        new_node = BSTNode(appointment)
        if not self.root:
            self.root = new_node  # If tree is empty, set the root
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        """Recursive helper function to insert a node."""
        if new_node.appointment['priority'] < current.appointment['priority']:
            if current.left:
                self._insert_recursive(current.left, new_node)
            else:
                current.left = new_node
        else:
            if current.right:
                self._insert_recursive(current.right, new_node)
            else:
                current.right = new_node

    def inorder_traversal(self, node):
        """In-order traversal to get appointments in sorted order based on priority."""
        if node:
            self.inorder_traversal(node.left)  # Visit left subtree
            print(f"Appointment ID: {node.appointment['id']}, Name: {node.appointment['name']}, Service: {node.appointment['service']}, Time: {node.appointment['time']}, Priority: {node.appointment['priority']}")
            self.inorder_traversal(node.right)  # Visit right subtree

    def find_appointment(self, appointment_id):
        """Find an appointment by ID."""
        return self._find_recursive(self.root, appointment_id)

    def _find_recursive(self, current, appointment_id):
        """Recursive helper function to find appointment by ID."""
        if current is None:
            return None
        if current.appointment['id'] == appointment_id:
            return current.appointment
        elif current.appointment['id'] > appointment_id:
            return self._find_recursive(current.left, appointment_id)
        else:
            return self._find_recursive(current.right, appointment_id)

# BST implementation
bst = AppointmentBST()

# Insert some appointments
bst.insert({"id": 1, "name": "John Doe", "service": "Haircut", "time": "10:00 AM", "priority": 3})
bst.insert({"id": 2, "name": "Jane Smith", "service": "Facial", "time": "11:00 AM", "priority": 1})
bst.insert({"id": 3, "name": "Emily Davis", "service": "Massage", "time": "2:00 PM", "priority": 5})

# Display appointments in sorted order based on priority (in-order traversal)
print("\nAppointments sorted by priority:")
bst.inorder_traversal(bst.root)

# Find a specific appointment by ID
appointment = bst.find_appointment(2)
if appointment:
    print(f"\nFound Appointment: {appointment}")
else:
    print("\nAppointment not found.")


