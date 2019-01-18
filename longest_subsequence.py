d = ["able", "ale", "apple", "bale", "kangaroo"]
s = "abppplee"

# Check longest Ds first - our first result will then be the longest and we can stop early
sorted_d = sorted(d, key=len, reverse=True)

def sub_of(candidate, sequence):
    if len(candidate) is 0:
        return True

    first_letter_idx = sequence.find(candidate[0])

    if first_letter_idx > -1:
        return sub_of(candidate[1:], sequence[first_letter_idx+1:])

    return False

for candidate in sorted_d:
    if sub_of(candidate, s):
        print candidate, 'is in', s
        break

