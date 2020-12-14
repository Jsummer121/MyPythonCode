# -*- coding: utf-8 -*-


def interpret(command):
    ans = ""
    while command:
        if command.startswith("G"):
            command = command.replace("G", "", 1)
            ans += "G"
        elif command.startswith("()"):
            command = command.replace("()", "", 1)
            ans += "o"
        else:
            command = command.replace("(al)", "", 1)
            ans += "al"
    return ans


if __name__ == '__main__':
    command = "G()(al)"
    interpret(command)
