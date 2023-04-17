class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def emplace(self, str):
        for i in range(len(str)):
            self.items.append(str[i])

    def get_stack(self):
        return self.items

