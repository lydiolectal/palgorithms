import unittest, heapq

def get_medians(l):
    low_heap = []
    high_heap = []
    cur_median = float("inf")
    medians = []
    for num in l:
        median = insert(num, l, low_heap, high_heap, cur_median)
        medians.append(median)
        cur_median = -low_heap[0]
    return medians

def insert(num, l, low_heap, high_heap, cur_median):
    if len(low_heap) > len(high_heap):
        if num < cur_median:
            temp = heapq.heappop(low_heap)
            heapq.heappush(low_heap, -num)
            heapq.heappush(high_heap, -temp)
        else:
            heapq.heappush(high_heap, num)
    else:
        if num < cur_median:
            heapq.heappush(low_heap, -num)
        else:
            heapq.heappush(high_heap, num)
            temp = heapq.heappop(high_heap)
            heapq.heappush(low_heap, -temp)
    median = -low_heap[0]
    return median

class TestMedian(unittest.TestCase):

    def test_two(self):
        l = [1, 2, 3]
        self.assertEqual(get_medians(l), [1, 1, 2])

    def test_three(self):
        l = [4, 1, 3, 2]
        self.assertEqual(get_medians(l), [4, 1, 3, 2])

    def test_fifteen(self):
        l = [4, 5, 6, 14, 9, 11, 2, 12, 7, 0, 10, 8, 13, 3, 1]
        expected = [4, 4, 5, 5, 6, 6, 6, 6, 7, 6, 7, 7, 8, 7, 8]

if __name__ == "__main__":

    unittest.main()

    l = []
    with open("median_maintenance.txt") as f:
         l = [int(i) for i in f.read().splitlines()]
         medians = get_medians(l)
    print(sum(medians))
