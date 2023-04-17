from Stack.stack import Stack


def decimal_to_binary():
    s = Stack()
    decimal = int(input())
    binary = ""

    while decimal > 0:
        s.push(decimal % 2)
        decimal //= 2

    for i in range(s.size()):
        binary += str(s.pop())

    print(binary)
