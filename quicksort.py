import unittest

def quicksort(l):
    if len(l) <= 1: 
        return l
    sort(l, 0, len(l))
    return l

def sort(l, low, high):
    if high - low > 1:
        pivot = l[high - 1]
        pivot_idx = low

        for i in range(low, high - 1):
            if l[i] < pivot:
                temp = l[i]
                l[i] = l[pivot_idx]
                l[pivot_idx] = temp
                pivot_idx += 1
        l[high - 1] = l[pivot_idx]
        l[pivot_idx] = pivot

        sort(l, low, pivot_idx)
        sort(l, pivot_idx + 1, high)

class TestQuickSort(unittest.TestCase):

    def test_empty_array(self):
        l = []
        result = quicksort(l)
        self.assertEqual(result, [])

    def test_single_elem(self):
        l = [6]
        result = quicksort(l)
        self.assertEqual(result, [6])

    def test_two_elems(self):
        l = [3, 0]
        result = quicksort(l)
        self.assertEqual(result, [0, 3])

    def test_three_elems(self):
        l = [3, 2, 1]
        result = quicksort(l)
        self.assertEqual(result, [1, 2, 3])

    def test_many_elems(self):
        l = [9, 1, 2, 6, 7, 8, 10, 11, 23, 90, 5, 9]
        result = quicksort(l)
        self.assertEqual(result, [1, 2, 5, 6, 7, 8, 9, 9, 10, 11, 23, 90])


if __name__ == "__main__":
    unittest.main()