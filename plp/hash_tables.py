from functools import reduce
from collections import Counter
import unittest

def frequencySort(s):
    counts = Counter()
    for c in s:
        counts[c] += 1
    ordered = counts.most_common()
    new_s = reduce(lambda a, c: a + c[0] * c[1], ordered, "")
    return new_s

def getHint(secret, guess):
    bulls = 0
    s_counts, g_counts = Counter(), Counter()
    for d in zip(secret, guess):
        if d[0] == d[1]:
            bulls += 1
        else:
            s_counts[d[0]] += 1
            g_counts[d[1]] += 1
    cows = reduce(lambda a, i: a + min(s_counts[i], g_counts[i]), [str(i) for i in range(10)], 0)
    return str(bulls) + "A" + str(cows) + "B"

class TestHashTables(unittest.TestCase):

    def test_freq_sort(self):
        s = "tree"
        self.assertIn(frequencySort(s), ["eert", "eetr"])

    def test_get_hint(self):
        secret = "1807"
        guess = "7810"
        self.assertEqual(getHint(secret, guess), "1A3B")
