def max_span(nums):
    idxes = {}
    span_lengths = {}
    max_span_length = 1

    for idx, num in enumerate(nums):
        if num not in idxes:
            # If this is the first instance of num, store its index and a span length of 1
            span_lengths[num] = 1
        else:
            # Otherwise, update the span length
            span_lengths[num] = span_lengths[num] - idxes[num] + idx

            # If a new span is found, check against the cached max and update if needed
            if span_lengths[num] > max_span_length:
                max_span_length = span_lengths[num]

        # Regardless, a new index for num has been found so store it
        idxes[num] = idx

    return max_span_length


print max_span([1, 2, 1, 1, 3]), 'should be 4'
print max_span([1, 4, 2, 1, 4, 1, 4]), 'should be 6'
print max_span([1, 4, 2, 1, 4, 4, 4]), 'should be 6'
