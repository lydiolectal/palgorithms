import unittest

def selectionsort(l):
    if len(l) <= 1:
        return l

    smallest = 0

    for i in range(len(l)):
        smallest = i

        for j in range(i, len(l)):
            if l[j] < l[smallest]:
                smallest = j
    
        temp = l[smallest]
        l[smallest] = l[i]
        l[i] = temp
    
    return l


class TestSelectionSort(unittest.TestCase):

    def test_empty_array(self):
        l = []
        result = selectionsort(l)
        self.assertEqual(result, [])

    def test_single_elem(self):
        l = [6]
        result = selectionsort(l)
        self.assertEqual(result, [6])

    def test_two_elems(self):
        l = [3, 0]
        result = selectionsort(l)
        self.assertEqual(result, [0, 3])

    def test_three_elems(self):
        l = [3, 2, 1]
        result = selectionsort(l)
        self.assertEqual(result, [1, 2, 3])

    def test_many_elems(self):
        l = [9, 1, 2, 6, 7, 8, 10, 11, 23, 90, 5, 9]
        result = selectionsort(l)
        self.assertEqual(result, [1, 2, 5, 6, 7, 8, 9, 9, 10, 11, 23, 90])


if __name__ == "__main__":
    unittest.main()