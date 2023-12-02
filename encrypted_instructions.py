import sys


def decode(commands: str) -> str:
    result: str = ''
    i: int = 0

    while i < len(commands):
        if commands[i].isalpha():
            result += commands[i]
            i += 1
        elif commands[i].isdigit():
            count_str: str = ''
            while commands[i].isdigit():
                count_str += commands[i]
                i += 1
            count: int = int(count_str)

            inner_command: str = ''
            i += 1
            len_section: int = 1

            while len_section != 0:
                inner_command += commands[i]

                if commands[i] == '[':
                    len_section += 1
                elif commands[i] == ']':
                    len_section -= 1

                i += 1

            decoded_inner_command = decode(inner_command[:-1])
            result += decoded_inner_command * count
    return result


if __name__ == '__main__':
    short_commands = sys.stdin.readline().rstrip()
    print(decode(short_commands))
