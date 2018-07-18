import unittest

def mergesort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]
    merged = merge(left, right)
    return merged

def merge(left, right):
    sorted_left = mergesort(left)
    sorted_right = mergesort(right)
    merged = []

    while sorted_left != [] or sorted_right != []:
        if sorted_left == [] or (sorted_right and sorted_right[0] < sorted_left[0]):
            merged.append(sorted_right[0])
            sorted_right = sorted_right[1:]
        else:
            merged.append(sorted_left[0])
            sorted_left = sorted_left[1:]

    return merged

class TestMergeSort(unittest.TestCase):

    def test_empty_array(self):
        l = []
        result = mergesort(l)
        self.assertEqual(result, [])

    def test_single_elem(self):
        l = [6]
        result = mergesort(l)
        self.assertEqual(result, [6])

    def test_two_elems(self):
        l = [3, 0]
        result = mergesort(l)
        self.assertEqual(result, [0, 3])

    def test_three_elems(self):
        l = [3, 2, 1]
        result = mergesort(l)
        self.assertEqual(result, [1, 2, 3])

    def test_many_elems(self):
        l = [9, 1, 2, 6, 7, 8, 10, 11, 23, 90, 5, 9]
        result = mergesort(l)
        self.assertEqual(result, [1, 2, 5, 6, 7, 8, 9, 9, 10, 11, 23, 90])


if __name__ == "__main__":
    unittest.main()
