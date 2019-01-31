def without_string(base, remove):
    output = []
    normalised_remove = remove.lower()
    remove_length = len(normalised_remove)

    normalised_base = base.lower()
    base_length = len(base)

    i = 0
    while i < base_length:
        candidate = normalised_base[i:i + remove_length]

        if candidate == normalised_remove:
            i += remove_length
            continue

        output.append(base[i])
        i += 1

    return ''.join(output)


print without_string("Hello there", "llo"), "Should be He there"
print without_string("Hello there", "e"), "Should be Hllo thr"
print without_string("Hello there", "x"), "Should be Hello there"
