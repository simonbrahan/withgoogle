def wordCount(words):
    output = {}
    for word in words:
        if word not in output:
            output[word] = 0

        output[word] += 1

    return output


print wordCount(["a", "b", "a", "c", "b"]), "Should be", {"a": 2, "b": 2, "c": 1}
print wordCount(["c", "b", "a"]), "Should be", {"a": 1, "b": 1, "c": 1}
print wordCount(["c", "c", "c", "c"]), "Should be", {"c": 4}
