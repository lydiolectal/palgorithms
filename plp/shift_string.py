import unittest

# shift the characters in a string k places to the right.
def shift(s, k):

    l = list(map(lambda idx: s[idx - k], range(0, len(s))))
    return "".join(l)

class TestStringShift(unittest.TestCase):

    def test_one_char(self):
        s = "h"
        k = 0
        self.assertEqual(shift(s, k), "h")

    def test_string(self):
        s = "hacker"
        k = 2
        self.assertEqual(shift(s, k), "erhack")

if __name__ == "__main__":
    unittest.main()
