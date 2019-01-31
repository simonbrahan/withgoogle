def pairs(words):
    output = {}
    for word in words:
        firstchar = word[0]
        if firstchar in output:
            continue

        output[firstchar] = word[-1]

    return output


print pairs(["code", "bug"]), "Should be ", {"b": "g", "c": "e"}
print pairs(["man", "moon", "main"]), "Should be", {"m": "n"}
print pairs(["man", "moon", "good", "night"]), "Should be", {"g": "d", "m": "n", "n": "t"}
