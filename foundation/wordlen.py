def wordLen(words):
    output = {}
    for word in words:
        if word in output:
            continue

        output[word] = len(word)

    return output


print wordLen(["a", "bb", "a", "bb"]), "Should be", {"bb": 2, "a": 1}
print wordLen(["this", "and", "that", "and"]), "Should be", {"that": 4, "and": 3, "this": 4}
print wordLen(["code", "code", "code", "bug"]), "Should be", {"code": 4, "bug": 3}
