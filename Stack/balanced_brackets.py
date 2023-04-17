from Stack.stack import Stack


def is_match(a, b):
    if a == "(" and b == ")":
        return True
    if a == "[" and b == "]":
        return True
    if a == "{" and b == "}":
        return True


def balanced_brackets():
    s = Stack()
    is_balanced = True
    parent_string = input()
    index = 0

    while is_balanced and index < len(parent_string):
        string = parent_string[index]
        if string in "([{":
            s.push(string)
        else:
            if s.empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, string):
                    is_balanced = False
                    break
        index += 1

    if is_balanced and s.empty():
        print("balanced")
    else:
        print("unbalanced")
