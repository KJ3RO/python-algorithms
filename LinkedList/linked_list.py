class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_allocator(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="")
            current_node = current_node.next

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def insert(previous_node, data):
        if not previous_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def remove(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        previous = None
        while current_node and current_node != key:
            previous = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous.next = current_node.next
        current_node = None

    def erase(self, position):
        if self.head:
            current_node = self.head

