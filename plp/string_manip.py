import unittest

def unique_morse_representations(words):
    unique_words = len(set(map(lambda w: morse_represent(w), words)))
    return unique_words

def morse_represent(word):
    codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
    ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
    "...","-","..-","...-",".--","-..-","-.--","--.."]
    morse_word = "".join(list(map(lambda c: codes[ord(c) - 97], list(word))))
    return morse_word

import unittest, functools

def substr(s, start, length):
    return s[start : start + length]

def replace_substr(s, start, length, target):
    return s[:start] + target + s[start + length:]

def findReplaceString(S, indexes, sources, targets):

    def substitute(acc, substitution):
        i, pattern, target = substitution
        if substr(S, i, len(pattern)) == pattern:
            acc = replace_substr(acc, i, len(pattern), target)
        return acc

    zipped = list(zip(indexes, sources, targets))
    to_replace = sorted(zipped, reverse = True)

    result = functools.reduce(substitute, to_replace, S)
    return result

class TestStringManip(unittest.TestCase):
    def test_morse_code(self):
        words = ["gin", "zen", "gig", "msg"]
        self.assertEqual(unique_morse_representations(words), 2)

    def test_leet(self):
        S = "abcd"
        indexes = [0,2]
        sources = ["a","cd"]
        targets = ["eee","ffff"]
        actual = findReplaceString(S, indexes, sources, targets)
        expected = "eeebffff"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
