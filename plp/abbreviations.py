import unittest

# bon
# [["b", "1"], ["bo", "1o", "2", "b1", "11"], ["bon", "1on", "2n", "b1n", "11n",
# "3", "b2", "12", "bo1", "1o1", "21", "b11", "111"]]

def abbrev(s):
    if len(s) < 1:
        return []
    memo = []
    first_abbrev = [s[0], "1"]
    memo.append(first_abbrev)
    for i in range(1, len(s)):
        abbrevs = []
        c = s[i]
        for abbrev in memo[i - 1]:
            new_abbrev = abbrev + c
            abbrevs.append(new_abbrev)
        abbrevs.extend(get_num_abbrevs(memo, i))
        memo.append(abbrevs)
    return memo[-1]

def get_num_abbrevs(memo, idx):
    num_abbrevs = []
    num_abbrevs.append(str(idx + 1))
    for i in range(idx):
        prev_abbrevs = memo[i]
        num_to_add = str(idx - i)
        for abbrev in prev_abbrevs:
            if not abbrev[-1].isdigit():
                new_abbrev = abbrev + num_to_add
                num_abbrevs.append(new_abbrev)
    return num_abbrevs

# 2, 5, 3, 1, 5, 6
# linear complexity
def get_max_diff(arr):
    if len(arr) == 0:
        return 0

    cur_min = arr[0]
    max_diff = 0

    for val in arr:
        if val < cur_min:
            cur_min = val
            continue
        diff = val - cur_min
        if diff > max_diff:
            max_diff = diff
    return max_diff

# O(n2) complexity
def get_max_diff_naive(arr):
    max_diff = 0

    for i in range(len(arr)):
        first = arr[i]
        for j in range(i, len(arr)):
            second = arr[j]
            diff = second - first
            if diff > max_diff:
                max_diff = diff

    return max_diff

class TestAbbrevs(unittest.TestCase):

    def test_two(self):
        s = "bo"
        abbrevs = abbrev(s)
        self.assertEqual(set(abbrevs), {"bo", "1o", "2", "b1"})

    def test_three(self):
        s = "bon"
        abbrevs = abbrev(s)
        expected = {"bon", "1on", "2n", "b1n",
        "3", "b2", "bo1", "1o1"}
        self.assertEqual(set(abbrevs), expected)

    def test_four(self):
        s = "word"
        abbrevs = abbrev(s)
        expected = {"word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d",
        "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"}
        self.assertEqual(set(abbrevs), expected)

    def test_eleven(self):
        s = "internation"
        abbrevs = abbrev(s)
        print(abbrevs)
