import unittest

# get number of ways to make change for n units using list c of denominations
def getWays(n, c):
    c = sorted(c)
    table = [[0 for _ in range(len(c))] for _ in range(n)]

    for row in range(n):
        t = row + 1
        for col, d in enumerate(c):
            x = t - d
            cur_ways = 0
            if x == 0:
                cur_ways = 1
            elif x > 0:
                cur_ways = table[x - 1][col]
            if col > 0:
                cur_ways += table[row][col - 1]
            table[row][col] = cur_ways
    return table[n - 1][len(c) - 1]

class TestChange(unittest.TestCase):

    def test_ways(self):
        self.assertEqual(getWays(3, [1, 2, 3, 8]), 3)
        self.assertEqual(getWays(4, [1, 2, 3]), 4)
        self.assertEqual(getWays(10, [2, 5, 3, 6]), 5)
