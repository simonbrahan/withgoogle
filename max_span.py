def max_span(nums):
    spans = {}

    for idx, num in enumerate(nums):
        if num not in spans:
            spans[num] = [idx-1, idx]
        else:
            spans[num][1] = idx

    span_sizes = map(lambda idxes: idxes[1] - idxes[0], spans.values())

    return max(span_sizes)


print max_span([1, 2, 1, 1, 3]), 'should be 4'
print max_span([1, 4, 2, 1, 4, 1, 4]), 'should be 6'
print max_span([1, 4, 2, 1, 4, 4, 4]), 'should be 6'
