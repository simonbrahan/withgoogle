# Unique binary tree
# Will store unique values only
# has flatten() method to return values as a list
class UBTree:
    @staticmethod
    def fromArr(arr):
        head, rest = arr[0], arr[1:]

        tree = UBTree(head)
        for i in rest:
            tree.offer(i)

        return tree

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def offer(self, val):
        # Discard duplicates
        if val == self.val:
            return False

        if val < self.val:
            return self.offerLeft(val)
        else:
            return self.offerRight(val)

    def offerLeft(self, val):
        if self.left is None:
            self.left = UBTree(val)
            return True
        else:
           return self.left.offer(val)

    def offerRight(self, val):
        if self.right is None:
            self.right = UBTree(val)
            return True
        else:
           return self.right.offer(val)

    def flatten(self):
        output = []

        if self.left is not None:
            output += self.left.flatten()

        output += [self.val]

        if self.right is not None:
            output += self.right.flatten()

        return output


def unique_sort(arr):
    if len(arr) == 0:
        return []

    tree = UBTree.fromArr(arr)
    return tree.flatten()


print unique_sort([])
print unique_sort([1, 1])
print unique_sort([1])
