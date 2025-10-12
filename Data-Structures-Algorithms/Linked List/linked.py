# Each node stores data and a link to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None   # first node (empty at start)

    # Add data at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:   # if list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:   # go to the last node
                current = current.next
            current.next = new_node

    # Show all elements
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Create a linked list
ll = LinkedList()

# Add some data
ll.append(10)
ll.append(20)
ll.append(30)

# Show the list
ll.display()
