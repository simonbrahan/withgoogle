def canbalance(arr):
    left_sum = 0
    target = sum(arr) / 2.0

    for num in arr:
        left_sum += num

        if left_sum == target:
            return True

    return False


print canbalance([1, 1, 1, 2, 1]), "Should be true"
print canbalance([2, 1, 1, 2, 1]), "Should be false"
print canbalance([10, 10]), "Should be true"
