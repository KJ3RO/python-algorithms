from Stack.stack import Stack


def base_to_base():
    s = Stack()
    input_number, base, new_base = input().split()
    base = int(base)
    new_base = int(new_base)
    decimal = 0
    final_value = ""

    factor = 1
    for i in range(len(input_number) - 1, -1, -1):
        if input_number[i] >= 'A':
            decimal += (ord(input_number[i]) - 55) * factor
        elif 0 <= int(input_number[i]) <= 9:
            decimal += int(input_number[i]) * factor
        factor *= base

    while decimal > 0:
        s.push(decimal % new_base)
        decimal //= new_base

    for i in range(s.size()):
        if 0 <= s.top() <= 9:
            final_value += str(s.pop())
        else:
            final_value += (hex(s.pop())[-1]).upper()

    print(final_value)
