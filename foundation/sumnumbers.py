def sumnumbers(string):
    current_sum = 0
    current_numeric_string = ''

    for char in string:
        if char.isdigit():
            current_numeric_string += char
            continue

        if len(current_numeric_string) > 0:
            current_sum += int(current_numeric_string)
            current_numeric_string = ''

    # Handle any numeric string left in buffer after reading input
    if len(current_numeric_string) > 0:
        current_sum += int(current_numeric_string)

    return current_sum


print sumnumbers("abc123xyz"), "Should be 123"
print sumnumbers("aa11b33"), "Should be 44"
print sumnumbers("7 11"), "Should be 18"
