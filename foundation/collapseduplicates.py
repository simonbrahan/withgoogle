def collapseDuplicates(a):
    output = ""
    last_char = None
    for char in a:
        if char == last_char:
            continue

        output += char
        last_char = char

    return output


print collapseDuplicates("a"), "Should be", "a"
print collapseDuplicates("aa"), "Should be", "a"
print collapseDuplicates("abbbbcc"), "Should be", "abc"
