def encoder(raw, code_words):
    output = []
    encodings = {}

    for word in raw:
        if word not in encodings:
            encodings[word] = code_words.pop(0)

        output.append(encodings[word])

    return output


print encoder(["a"], ["1", "2", "3", "4"]), "Should be", ["1"]
print encoder(["a", "b"], ["1", "2", "3", "4"]), "Should be", ["1", "2"]
print encoder(["a", "b", "a"], ["1", "2", "3", "4"]), "Should be", ["1", "2", "1"]
