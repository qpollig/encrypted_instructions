import sys


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)


# line = 3[a2[c]]; retern ассассасс
def find_section(stack, line, left_pointer, right_pointer, arr: list[str]):
    open_brackets = '['
    close_brackets = ']'
    for char in line:
        if char is open_brackets:
            stack.push(char)
        elif char is close_brackets:
            left_pointer = stack.peek() + 1
            right_pointer = line.index(char, left_pointer)
            find_section(stack, line, left_pointer, right_pointer)
        else:
            num = stack.peek() - 1
            section = line[left_pointer:right_pointer] * num
            arr.append(section)
    return arr


def decoding(line: str) -> str:
    stack = Stack()
    left_pointer = 0
    right_pointer = 0
    arr = []
    decode_arr = find_section(stack, line, left_pointer, right_pointer, arr)
    return decode_arr


if __name__ == '__main__':
    str_line = sys.stdin.readline().rstrip()
    print(decoding(str_line))



