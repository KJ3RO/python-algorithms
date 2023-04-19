from Stack.balanced_brackets import balanced_brackets
from Stack.decimal_to_binary import decimal_to_binary
from Stack.base_to_base import base_to_base
from LinkedList.linked_list import LinkedList


def main():
    a = LinkedList()
    a.push_back("A")
    a.push_back("B")
    a.push_back("C")
    a.push_back("D")

    a.swap("B", "C")
    print("Swapping nodes B and C that are not head nodes")
    a.get_allocator()


if __name__ == '__main__':
    main()
