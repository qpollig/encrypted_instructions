# 2 дек 2023, 23:14:11 101268990 OK 51ms 4.25Mb
import sys


def decode(line_command: str) -> str:
    line_decode: str = ''
    i: int = 0
    while i < len(line_command):
        if line_command[i].isalpha():
            line_decode += line_command[i]
            i += 1
        elif line_command[i].isdigit():
            count_str: str = ''
            while line_command[i].isdigit():
                count_str += line_command[i]
                i += 1
            count: int = int(count_str)
            inner_command: str = ''
            i += 1
            len_section: int = 1

            while len_section != 0:
                inner_command += line_command[i]

                if line_command[i] == '[':
                    len_section += 1
                elif line_command[i] == ']':
                    len_section -= 1
                i += 1

            decoded_inner_command = decode(inner_command[:-1])
            line_decode += decoded_inner_command * count
    return line_decode


if __name__ == '__main__':
    commands = sys.stdin.readline().rstrip()
    print(decode(commands))
