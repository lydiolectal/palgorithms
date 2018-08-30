import unittest, heapq

def get_medians(l):
    low_heap = []
    high_heap = []
    cur_median = float("inf")
    medians = []
    for num in l:
        median = insert(num, l, low_heap, high_heap, cur_median)
        medians.append(median)
        cur_median = low_heap[0]
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
            temp = heapq.heappop(high_heap)
            heapq.heappush(high_heap, -num)
            heapq.heappush(low_heap, -temp)
    median = -low_heap[0]
    return median

class TestMedian(unittest.TestCase):

    def test_two(self):
        l = [1, 2, 3]
        self.assertEqual(get_medians(l), [1, 1, 2])

    def test_three(self):
        l = [1, 2, 3, 4]
        self.assertEqual(get_medians(l), [1, 1, 2, 2])

if __name__ == "__main__":

     # with open("median_maintenance.txt") as f:
     #     l = [int(i) for i in f.read().splitlines()]
     #     print(str(l[0]))

    unittest.main()
