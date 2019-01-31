def word0(words):
    output = {}
    for word in words:
        output[word] = 0

    return output


print word0(["a", "b", "a", "b"]), "Should be", {"a": 0, "b": 0}
print word0(["a", "b", "a", "c", "b"]), "Should be", {"a": 0, "b": 0, "c": 0}
print word0(["c", "b", "a"]), "Should be ", {"a": 0, "b": 0, "c": 0}
