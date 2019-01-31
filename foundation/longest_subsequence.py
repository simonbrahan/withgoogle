d = ["able", "ale", "bale", "kangaroo", "apple"]
s = "abppplee"

# Check longest Ds first - our first result will then be the longest and we can stop early
sorted_d = sorted(d, key=len, reverse=True)

# Global sequence cache populated by parse_sequence
sequence_cache = {}

class SequenceMap:
    def __init__(self, sequence_str):
        self.sequence_index = {}
        for char_idx, char in enumerate(sequence_str):
            if char not in self.sequence_index:
                self.sequence_index[char] = []
            self.sequence_index[char].append(char_idx)


    def find(self, char):
        if char not in self.sequence_index:
            return -1

        return self.sequence_index[char][0]


def parse_sequence(sequence_str):
    if sequence_str not in sequence_cache:
        sequence_cache[sequence_str] = SequenceMap(sequence_str)

    return sequence_cache[sequence_str]


def get_first_occurence(char, sequence):
    sequence_map = parse_sequence(sequence)
    return sequence.find(char)


def tail(string, idx = 0):
    return string[idx+1:]


def sub_of(candidate, sequence):
    if len(candidate) is 0:
        return True

    first_letter_idx = get_first_occurence(candidate[0], sequence)

    if first_letter_idx == -1:
        return False

    return sub_of(tail(candidate), tail(sequence, first_letter_idx))


for candidate in sorted_d:
    if sub_of(candidate, s):
        print candidate, 'is in', s
        break

