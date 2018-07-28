import unittest

class TrieNode:

    def __init__(self):
        self.isWord = False
        self.children = {}

    def insert(self, word, curr = ""):
        if len(word) > 0:
            curr += word[0]
            if curr not in self.children:
                self.children[curr] = TrieNode()
            self.children[curr].insert(word[1:], curr)
        else:
            self.isWord = True

    def contains(self, word, curr = ""):
        if len(word) > 0:
            curr += word[0]
            if curr in self.children:
                return self.children[curr].contains(word[1:], curr)
            else:
                return False
        else:
            return self.isWord

def longest_word(words):
    root = TrieNode()
    for word in words:
        root.insert(word)
    longest = ""
    def find_longest(curr):
        nonlocal longest
        for string, child in curr.children.items():
            if child.isWord:
                if len(string) > len(longest) or \
                  (len(string) == len(longest) and string < longest):
                    longest = string
                find_longest(child)
    find_longest(root)
    return longest

class TestLongestWord(unittest.TestCase):
    def test_world(self):
        words = ["w","wo","wor","worl", "world"]
        self.assertEqual(longest_word(words), "world")

    def test_apple(self):
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        self.assertEqual(longest_word(words), "apple")

    def test_trie(self):
        t = TrieNode()
        t.insert("hi!")
        self.assertTrue(t.contains("hi!"))

    def test_trie_more(self):
        t = TrieNode()
        t.insert("a")
        t.insert("app")
        self.assertTrue(t.contains("app"))
        self.assertFalse(t.contains("ap"))
