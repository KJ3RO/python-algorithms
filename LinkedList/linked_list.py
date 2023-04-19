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
            if position == 0:
                self.head = current_node.next
                current_node = None
                return
            
            previous = None
            count = 0
            while current_node and count != position:
                previous = current_node
                current_node = current_node.next
                count += 1

            if current_node is None:
                return
            
            previous.next = current_node.next
            current_node = None

    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.next)
    
    def swap(self, key1, key2):
        if key1 == key2:
            return
        
        previous1 = None
        current1 = self.head
        while current1 and current1.data != key1:
            previous1 = current1
            current1 = current1.next
            
        previous2 = None
        current2 = self.head
        while current2 and current2.data != key2:
            previous2 = current2
            current2 = current2.next
        
        if not current1 or not current2:
            return
        
        if previous1:
            previous1.next = current2
        else:
            self.head = current2
            
        if previous2:
            previous2.next = current1
        else:
            self.head = current1
        
        current1.next, current2.next = current2.next, current1.next
            

        
