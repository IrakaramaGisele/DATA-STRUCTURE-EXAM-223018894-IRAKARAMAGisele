class TreeNode:
    def __init__(self, data):
        self.data = data  # Data could be department, employee, or appointment info
        self.children = []  # List to store child nodes

    def add_child(self, child_node):
        """Add a child node to the current node."""
        self.children.append(child_node)

    def remove_child(self, child_node):
        """Remove a child node from the current node."""
        for idx, child in enumerate(self.children):
            if child.data == child_node.data:
                del self.children[idx]
                return
        print(f"Node '{child_node.data}' not found under '{self.data}'.")

    def display(self, level=0):
        """Recursively display the tree structure with indentation to show hierarchy."""
        indent = "  " * level
        print(f"{indent}- {self.data}")
        for child in self.children:
            child.display(level + 1)


class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)  # The root node represents the salon

    def display_tree(self):
        """Display the entire tree starting from the root."""
        self.root.display()

    def add_node(self, parent_data, child_data):
        """Add a new node under a parent node."""
        parent_node = self.find_node(self.root, parent_data)
        if parent_node:
            child_node = TreeNode(child_data)
            parent_node.add_child(child_node)
        else:
            print(f"Parent node '{parent_data}' not found.")

    def remove_node(self, parent_data, child_data):
        """Remove a child node from a parent node."""
        parent_node = self.find_node(self.root, parent_data)
        if parent_node:
            child_node = self.find_node(parent_node, child_data)
            if child_node:
                parent_node.remove_child(child_node)
            else:
                print(f"Child node '{child_data}' not found.")
        else:
            print(f"Parent node '{parent_data}' not found.")

    def find_node(self, node, data):
        """Find a node by its data (recursively)."""
        if node.data == data:
            return node
        for child in node.children:
            result = self.find_node(child, data)
            if result:
                return result
        return None


# Example usage for Tree (Salon Appointment Management)
salon_tree = Tree("Salon")

# Add departments
salon_tree.add_node("Salon", "Haircuts")
salon_tree.add_node("Salon", "Facials")
salon_tree.add_node("Salon", "Massages")

# Add employees to departments
salon_tree.add_node("Haircuts", "John Doe")
salon_tree.add_node("Haircuts", "Alice Green")
salon_tree.add_node("Facials", "Jane Smith")
salon_tree.add_node("Massages", "Emily Davis")

# Add appointments for employees
salon_tree.add_node("John Doe", "Haircut at 10:00 AM")
salon_tree.add_node("John Doe", "Haircut at 2:00 PM")
salon_tree.add_node("Jane Smith", "Facial at 11:00 AM")
salon_tree.add_node("Emily Davis", "Massage at 1:00 PM")

# Display the entire salon structure (tree)
print("Salon Appointment Management System:")
salon_tree.display_tree()

# Remove an appointment and display the updated tree
salon_tree.remove_node("John Doe", "Haircut at 2:00 PM")
print("\nAfter removing an appointment:")
salon_tree.display_tree()

# Try to remove a non-existing node
salon_tree.remove_node("Haircuts", "Non-existent Employee")


