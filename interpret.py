def interpret(value, commands, args):
    for command, arg in zip(commands, args):
        if command == "+":
            value += arg
        elif command == "-":
            value -= arg
        elif command == '*':
            value *= arg
        else:
            return -1

    return value


print interpret(1, ["+"], [1]), "Should be 2"
print interpret(4, ["-"], [2]), "Should be 2"
print interpret(1, ["+", "*"], [1, 3]), "Should be 6"
print interpret(1, ['+'], [1]), "Should be 2"
print interpret(4, ['-'], [2]), "Should be 2"
print interpret(1, ['+', '*'], [1, 3]), "should be 6"
