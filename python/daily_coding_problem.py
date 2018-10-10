import unittest
import functools

# Day 1
# Given a list of numbers and a number k, return whether any two numbers
# from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def add_to_k(l, k):
    nums = set()
    for num in l:
        diff = k - num
        if diff in nums:
            return True
        nums.add(num)
    return False

# Day 2
# Given an array of integers, return a new array such that each element at index
# i of the new array is the product of all the numbers in the original array
# except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
# be [2, 3, 6].
#
# Follow-up: what if you can't use division?

def arr_product(l):
    total_prod = functools.reduce(lambda x, y: x * y, l)
    new_l = list(map(lambda x: total_prod // x, l))
    return new_l

# TODO: constrained version.


# Day 4
# Given an array of integers, find the first missing positive integer in
# linear time and constant space. In other words, find the lowest positive
# integer that does not exist in the array. The array can contain duplicates
# and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
# should give 3.
#
# You can modify the input array in-place.

def first_missing_int(arr):
    length = len(arr)
    for i in range(len(arr)):
        num = arr[i]
        while num > 0 and num <= length and num - 1 != i:
            temp = arr[num - 1]
            arr[num - 1] = num
            arr[i] = temp
            num = temp
    for i, num in enumerate(arr):
        if num != i + 1:
            return i + 1

    return length + 1


# Day 5
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first
# and last element of that pair. For example, car(cons(3, 4)) returns 3,
# and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def take_car(a, b):
        return a

    return pair(take_car)

def cdr(pair):
    def take_cdr(a, b):
        return b

    return pair(take_cdr)

# Day 7
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
# count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as
# 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not
# allowed.
# seems similar to the dynamic programming problem of "1 or 2 steps on a
# staircase" but with filtering

# recursive solution
def decode(m):
    calculated = [0 for _ in range(len(m))]
    def helper(idx):
        # check 'cache'
        if calculated[idx]:
            return calculated[idx]

        # base cases
        if idx == 0:
            calculated[0] = 1
            return 1
        if idx == 1:
            if int(m[:2]) <= 26:
                calculated[1] = 2
                return 2
            calculated[1] = 1
            return 1

        # recursive case
        mappings = helper(idx - 1)
        if int(m[idx - 1:idx + 1]) <= 26:
            mappings += helper(idx - 2)
        calculated[idx] = mappings
        return mappings
    return helper(len(m) - 1)

# Day 8
# A unival tree is a tree where all nodes under it have the same value
# Given a root to a binary tree, count the number of unival subtrees
# for instance, the following tree has 5 unival subtrees:
#     0
#   /  \
#  1    0
#     /  \
#   1   0
#  / \
# 1   1
#

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_trees(root):
    count = 0
    def count_subtrees(curr):
        nonlocal count
        if curr == None:
            return True

        l_unival = count_subtrees(curr.left)
        r_unival = count_subtrees(curr.right)
        if curr.left and curr.val != curr.left.val:
            l_unival = False
        if curr.right and curr.val != curr.right.val:
            r_unival = False

        if l_unival and r_unival:
            count += 1
            return True
    count_subtrees(root)
    return count

# Day 9
# Given a list of integers, write a function that returns the largest sum of
# non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?
# straightforward dynamic programming approach.

# linear time and linear space
def largest_nonadjacent_sum(l):
    size = len(l)
    sums = [0] * size
    # handle edge cases of 0, 1 indices
    if size <= 2:
        return max(l)
    sums[0], sums[1] = l[0], max(l[0], l[1])

    for i in range(2, size):
        prev = sums[i - 1]
        curr = sums[i - 2] + l[i]
        sums[i] = max(prev, curr)

    return sums[size - 1]

# linear time and constant space
def largest_nonadjacent_sum_efficient(l):
    size = len(l)
    if size <= 2:
        return max(l)

    prev_prev, prev = l[0], max(l[:2])
    for num in l[2:]:
        new = max(prev, prev_prev + num)
        prev_prev = prev
        prev = new
    return prev

# Day 10
# Implement a job scheduler which takes in a function f and an integer n,
# and calls f after n milliseconds.
# TODO: check if this is even right?

def schedule_job(f, n):
    time.sleep(n/1000)
    f()

# Day 11
# Implement an autocomplete system. That is, given a query string s and a set of
# all possible query strings, return all strings in the set that have s as a
# prefix.
#
# For example, given the query string de and the set of strings [dog, deer,
# deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to
# speed up queries.

class TrieNode:

    def __init__(self):
        self.children = {}
        self.words = []

    def insert(self, word, i):
        if i < len(word):
            cur = word[i]
            self.words.append(word)
            if cur not in self.children:
                self.children[cur] = TrieNode()
            self.children[cur].insert(word, i + 1)
        else:
            self.words.append(word)

def insert_list(root, l):
    for word in l:
        root.insert(word, 0)

def autocomplete(s, words):
    root = TrieNode()
    insert_list(root, words)

    cur_node = root
    for c in s:
        if c in cur_node.children:
            cur_node = cur_node.children[c]
        else:
            return []

    return cur_node.words

# Day 12
#
# There exists a staircase with N steps, and you can climb up either 1 or 2
# steps at a time. Given N, write a function that returns the number of unique
# ways you can climb the staircase. The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could
# climb any number from a set of positive integers X? For example, if X =
# {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

def climb(n):
    ways = [0] * (n + 1)
    def helper(n):
        if ways[n]:
            return ways[n]
        if n <= 2:
            ways[n] = n
            return n

        way = helper(n - 1) + helper(n - 2)
        ways[n] = way
        return way

    helper(n)
    return ways[n]

def climb_extended(n, steps):
    pass

# Day 13

# Given an integer k and a string s, find the length of the longest substring
# that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k
# distinct characters is "bcb".
def longest_substring(k, s):
    if len(s) == 0 or k < 1:
        return ""

    start, end = 0, 0
    cur_chars = {}
    cur_longest = ""
    while end < len(s):
        add_char(s[end], cur_chars)
        if len(cur_chars) > k:
            temp_length = end - start + 1
            if temp_length > len(cur_longest):
                cur_longest = s[start:end]
            while len(cur_chars) > k:
                remove_char(s[start], cur_chars)
                start += 1
        end = end + 1
    if len(cur_chars) <= k and end - start > len(cur_longest):
        cur_longest = s[start:end]
    return cur_longest

def remove_char(c, cur_chars):
    if cur_chars[c] == 1:
        cur_chars.pop(c)
    else:
        cur_chars[c] -= 1

def add_char(c, cur_chars):
    if c in cur_chars:
        cur_chars[c] += 1
    else:
        cur_chars[c] = 1

# Day 16
# You run an e-commerce website and want to record the last N order ids in a
# log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be
# smaller than or equal to N.
# You should be as efficient with time and space as possible.
# I think this is a binary search tree problem.

class OrderLog:

    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.offset = 0

    def record(self, order_id):
        if len(self.arr) < self.capacity:
            self.arr.append(order_id)
        else:
            self.arr[self.offset] = order_id
            self.offset = (self.offset + 1) % self.capacity

    def get_last(self, i):
        idx = (self.capacity - i + self.offset) % self.capacity
        return self.arr[idx]

# Day 17 TODO
# Suppose we represent our file system by a string in the following manner:
#
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory
# subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t
# \tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1
# contains a file file1.ext and an empty second-level sub-directory subsubdir1.
# subdir2 contains a second-level sub-directory subsubdir2 containing a file
# file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path
# to a file within our file system. For example, in the second example above,
# the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its
# length is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the
# length of the longest absolute path to a file in the abstracted file system.
# If there is no file in the system, return 0.
#
# Note:
#
# The name of a file contains at least a period and an extension.
#
# The name of a directory or sub-directory will not contain a period.

def longest_filepath(path):
    pass

# Day 18
# Given an array of integers and a number k, where 1 <= k <= length of the
# array, compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
# [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place
# and you do not need to store the results. You can simply print them out as you
# compute them.
# hunch: "max" queue.
def max_subarray(arr, k):
    max_q = []
    pass

# Day 19 TODO
# A builder is looking to build a row of N houses that can be of K different
# colors. He has a goal of minimizing cost while ensuring that no two
# neighboring houses are of the same color.
#
# Given an N by K matrix where the nth row and kth column represents the cost to
# build the nth house with kth color, return the minimum cost which achieves
# this goal.
# Hunch: dynamic programming, where you track the "cheapest" route to get to
# each color for each level. Do layer by layer.

# Day 21
# Given an array of time intervals (start, end) for classroom lectures (possibly
# overlapping), find the minimum number of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
# idea: sort the ranges by start value (then end value). step through number
# line and return max range overlaps over the range (smallest_start, largest_end)

def min_rooms(intervals):
    if len(intervals) == 0:
        return 0

    intervals.sort()
    cur_start, cur_end = intervals[0]
    cur_overlap = 0
    highest_overlap = 1
    for i in range(len(intervals)):
        start, end = intervals[i]
        # is an overlap
        if start < cur_end:
            cur_start = start
            cur_end = min(end, cur_end)
            cur_overlap += 1
        # no overlap
        else:
            highest_overlap = max(highest_overlap, cur_overlap)
            cur_overlap = 0
            idx = i
            cur_start, cur_end = start, end
            while idx >= 0:
                start, end = intervals[idx]
                if end <= cur_start:
                    break
                cur_end = min(end, cur_end)
                cur_overlap += 1
                idx -= 1
    return max(cur_overlap, highest_overlap)

# Day 22
# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible
# reconstruction, return any of them. If there is no possible reconstruction,
# then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
# string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
# string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
# ['bedbath', 'and', 'beyond']
# hunch: use trie to store dictionary, traverse for each word.

class AnotherTrieNode:

    def __init__(self):
        self.children = {}
        self.is_terminal = False

def reconstruct_sentence(words, s):
    # insert words into trie
    root = AnotherTrieNode()
    for word in words:
        insert_word(root, word)

    parsings = []
    def reconstruct(wordlist, s):
        nonlocal parsings
        if s == "":
            parsings.append(wordlist)
            return
        # traverse trie until you reach a terminal node
        c = s[0]
        s = s[1:]
        curnode = root
        word = ""
        while c in curnode.children:
            curnode = curnode.children[c]
            word += c
            if curnode.is_terminal:
                wordlist.append(word)
                reconstruct(wordlist, s)
                wordlist = wordlist[:-1]
            if s:
                c = s[0]
                s = s[1:]
            else:
                break

    reconstruct([], s)
    if parsings:
        return parsings[0]
    return None

def insert_word(node, w):
    if not w:
        node.is_terminal = True
        return
    c = w[0]
    if c not in node.children:
        new_node = AnotherTrieNode()
        node.children[c] = new_node
    insert_word(node.children[c], w[1:])

# Day 23
# You are given an M by N matrix consisting of booleans that represents a board.
# Each True boolean represents a wall. Each False boolean represents a tile you
# can walk on.

# Given this matrix, a start coordinate, and an end coordinate, return the
# minimum number of steps required to reach the end coordinate from the start.
# If there is no possible path, then return null. You can move up, left, down,
# and right. You cannot move through walls. You cannot wrap around the edges of
# the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum
# number of steps required to reach the end is 7, since we would need to go
# through (1, 2) because there is a wall everywhere else on the second row.
# hunch: breadth first search.

# Day 25
# Implement regular expression matching with the following special characters:
#
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular
# expression and returns whether or not the string matches the regular
# expression.
#
# For example, given the regular expression "ra." and the string "ray", your
# function should return true. The same regular expression on the string
#"raymond" should return false.
#
# Given the regular expression ".*at" and the string "chat", your function
# should return true. The same regular expression on the string "chats" should
# return false.
# assumes a legal regex; ie, "*" does not start the regex and "." is not a char.

def is_match(token, c):
    if token == ".":
        return True
    else:
        return token == c

def match_regex(re, s):
    match = False
    def helper(re, s, re_idx, s_idx):
        nonlocal match
        # scan through string and re in parallel and call helper when ambiguity
        # arises.
        if re_idx == len(re) and s_idx == len(s):
            match = True
            return
        elif re_idx == len(re) or s_idx == len(s):
            return
        token, ast = re[re_idx]
        char = s[s_idx]
        matches = is_match(token, char)
        if ast:
            helper(re, s, re_idx + 1, s_idx)
            if matches:
                helper(re, s, re_idx, s_idx + 1)
                helper(re, s, re_idx + 1, s_idx + 1)
        elif not ast and matches:
            helper(re, s, re_idx + 1, s_idx + 1)
        else:
            return

    rich_re = []
    i = 0
    while i < len(re):
        if i < len(re) - 1 and re[i + 1] == "*":
            rich_re.append((re[i], True))
            i += 1
        else:
            rich_re.append((re[i], False))
        i += 1
    helper(rich_re, s, 0, 0)
    return match

# Day 26
# Given a singly linked list and an integer k, remove the kth last element
# from the list. k is guaranteed to be smaller than the length of the list.
#
# The list is very long, so making more than one pass is prohibitively
# expensive.
#
# Do this in constant space and in one pass.
# my solution: does not take up constant space because recursion.
# iterative solution: use a fast pointer that's k ahead of slow pointer.
# move fast to end of list to "measure" k steps away from last node.

class LinkedListNode:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def remove_kth_last(k, node):
    if not node.next:
        return k

    idx_from_last = remove_kth_last(k, node.next)
    if idx_from_last == 1:
        node.next = node.next.next
    idx_from_last -= 1
    return idx_from_last

# Day 27
# Given a string of round, curly, and square open and closing brackets, return
# whether the brackets are balanced (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.
# assumes all input is a bracket.
def is_well_formed(parens):
    oparens = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for paren in parens:
        if paren in pairs:
            if len(oparens) == 0 or oparens.pop() != pairs[paren]:
                return False
        else:
            oparens.append(paren)
    return len(oparens) == 0

# Day 28
# Write an algorithm to justify text. Given a sequence of words and an integer
# line length k, return a list of strings which represents each line, fully
# justified.

# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word. Pad extra spaces when
# necessary so that each line has exactly length k. Spaces should be distributed
# as equally as possible, with the extra spaces, if any, distributed starting
# from the left.
#
# If you can only fit one word on a line, then you should pad the right-hand
# side with spaces.
#
# Each word is guaranteed not to be longer than k.
#
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps",
# "over", "the", "lazy", "dog"] and k = 16, you should return the following:
#
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

# Day 29
# Run-length encoding is a fast and simple method of encoding strings. The basic
# idea is to represent repeated successive characters as a single count and
# character. For example, the string "AAAABBBCCDAA" would be encoded as
# "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be
# encoded have no digits and consists solely of alphabetic characters. You can
# assume the string to be decoded is valid.

# Day 30
# You are given an array of non-negative integers that represents a
# two-dimensional elevation map where each element is unit-width wall and the
# integer is the height. Suppose it will rain and all spots between two walls
# get filled up.
#
# Compute how many units of water remain trapped on the map in O(N) time and
# O(1) space.
#
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the
# middle.
#
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2
# in the second, and 3 in the fourth index (we cannot hold 5 since it would run
# off to the left), so we can trap 8 units of water.
# [3, 0, 1, 3, 0, 1, 0] => 3 + 2 + 1

def rain_trapped(elev_map):
    peak = 0
    interval = []
    rain_trapped = 0
    for unit in elev_map:
        # if new peak (>= peak) found, pop volume trapped so far into
        # rain_trapped and reset peak to new peak
        if unit >= peak:
            rain_trapped += pop_volume(interval, peak)
            interval = [unit]
            peak = unit
        else:
            interval.append(unit)
    # pop volumes off interval in reverse when you hit end of elev_map
    if len(interval) > 1:
        mini_interval = []
        peak = 0
        while len(interval) > 0:
            unit = interval.pop()
            if unit >= peak:
                rain_trapped += pop_volume(mini_interval, peak)
                mini_interval = [unit]
                peak = unit
            else:
                mini_interval.append(unit)
    return rain_trapped

def pop_volume(interval, min_peak):
    volume = functools.reduce(lambda s, v: s + min_peak - v, interval, 0)
    return volume

# Day 34
# Given a string, find the palindrome that can be made by inserting the fewest
# number of characters as possible anywhere in the word. If there is more than
# one palindrome of minimum length that can be made, return the
# lexicographically earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we
# can add three letters to it (which is the smallest amount to make a
# palindrome). There are seven other palindromes that can be made from "race"
# by adding three letters, but "ecarace" comes first alphabetically.
#
# As another example, given the string "google", you should return "elgoogle".

def smallest_palindrome(word):
    possible_dromes = []


# Day 35
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the
# values of the array so that all the Rs come first, the Gs come second, and the
# Bs come last. You can only swap elements of the array.
#
# Do this in linear time and in-place.
#
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
# become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def sort_rgb(arr):
    # separate Rs from Gs and Bs
    rpartition = 0
    for i in range(len(arr)):
        if arr[i] == 'R':
            arr[rpartition], arr[i] = arr[i], arr[rpartition]
            rpartition += 1

    gpartition = rpartition
    for i in range(rpartition, len(arr)):
        if arr[i] == 'G':
            arr[gpartition], arr[i] = arr[i], arr[gpartition]
            gpartition += 1

    return arr

# Day 36
# Given the root to a binary search tree, find the second largest node in the
# tree.

# Day 37
# The power set of a set is the set of all its subsets. Write a function that,
# given a set, generates its power set.
#
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3},
# {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
#
# You may also use a list or array to represent a set.

def power_set():
    pass

# Day 38
# You have an N by N board. Write a function that, given N, returns the number
# of possible arrangements of the board where N queens can be placed on the
# board without threatening each other, i.e. no two queens share the same row,
# column, or diagonal.

# Day 39

# -------------------------------
# some tests
class TestDailies(unittest.TestCase):

    def test_1(self):
        l = [10, 15, 3, 7]
        k = 17
        result = add_to_k(l, k)
        self.assertTrue(result)

        l = [10, 15, 3, 7]
        k = 11
        result = add_to_k(l, k)
        self.assertFalse(result)

    def test_2(self):
        l = [1, 2, 3, 4, 5]
        result = arr_product(l)
        expected = [120, 60, 40, 30, 24]
        self.assertEqual(result, expected)

    def test_4(self):
        arr = [3, 4, 1, -1]
        result = first_missing_int(arr)
        expected = 2
        self.assertEqual(result, expected)

        arr = [1, 2, 0]
        result = first_missing_int(arr)
        expected = 3
        self.assertEqual(result, expected)

        arr = [1, 2, 3]
        result = first_missing_int(arr)
        expected = 4
        self.assertEqual(result, expected)

        arr = [4, 1, 5, 6, 2]
        result = first_missing_int(arr)
        expected = 3
        self.assertEqual(result, expected)

    def test_5(self):
        a, b = 1, 2
        pair = cons(a, b)
        result = car(pair)
        expected = 1
        self.assertEqual(result, expected)

        result = cdr(pair)
        expected = 2
        self.assertEqual(result, expected)

    def test_7(self):
        message = "111"
        result = decode(message)
        expected = 3
        self.assertEqual(result, expected)

        message = "192"
        result = decode(message)
        expected = 2
        self.assertEqual(result, expected)

        message = "11926"
        # 1, 1, 2, 3, 6
        # 1, 1, 9, 26
        # 11, 9, 26
        # 11, 9, 2, 6
        # 1, 19, 2, 6
        # 1, 19, 26
        result = decode(message)
        expected = 6
        self.assertEqual(result, expected)

    def test_8(self):
        left = Node(0)
        right = Node(1)
        root = Node(0, left, right)

        result = count_unival_trees(root)
        expected = 2
        self.assertEqual(result, expected)

        rll = Node(1)
        rlr = Node(1)
        rl = Node(1, rll, rlr)
        rr = Node(0)
        r = Node(0, rl, rr)
        l = Node(1)
        root = Node(0, l, r)

        result = count_unival_trees(root)
        expected = 5
        self.assertEqual(result, expected)

    def test_9(self):
        l = [2, 4, 6, 2, 5]
        result = largest_nonadjacent_sum(l)
        expected = 13
        self.assertEqual(result, expected)

        l = [5, 1, 1, 5]
        result = largest_nonadjacent_sum(l)
        expected = 10
        self.assertEqual(result, expected)

        l = [6, 4, -3, 2, 5]
        result = largest_nonadjacent_sum(l)
        expected = 11
        self.assertEqual(result, expected)

    def test_9_efficient(self):
        l = [2, 4, 6, 2, 5]
        result = largest_nonadjacent_sum_efficient(l)
        expected = 13
        self.assertEqual(result, expected)

        l = [5, 1, 1, 5]
        result = largest_nonadjacent_sum_efficient(l)
        expected = 10
        self.assertEqual(result, expected)

        l = [6, 4, -3, 2, 5]
        result = largest_nonadjacent_sum_efficient(l)
        expected = 11
        self.assertEqual(result, expected)

    def test_10(self):
        s = "de"
        words = ["deer", "deal", "dog"]
        result = autocomplete(s, words)
        expected = ["deer", "deal"]
        self.assertEqual(result, expected)

    def test_12(self):
        result = climb(4)
        expected = 5
        self.assertEqual(result, expected)

    def test_13(self):
        result = longest_substring(2, "abcba")
        expected = "bcb"
        self.assertEqual(result, expected)

        result = longest_substring(3, "abcdaaabcc")
        expected = "aaabcc"
        self.assertEqual(result, expected)

    def test_16(self):
        log = OrderLog(3)
        log.record(1)
        log.record(2)
        log.record(3)
        expected = 1
        result = log.get_last(3)
        self.assertEqual(result, expected)

        log.record(4)
        expected = 4
        result = log.get_last(1)
        self.assertEqual(result, expected)

        expected = [4, 2, 3]
        result = log.arr
        self.assertEqual(result, expected)

    def test_21(self):
        ranges = [(30, 75), (0, 50), (60, 150)]
        result = min_rooms(ranges)
        expected = 2
        self.assertEqual(result, expected)

        ranges = [(0, 5), (2, 8), (3, 11), (5, 10), (5, 11)]
        result = min_rooms(ranges)
        expected = 4
        self.assertEqual(result, expected)

    def test_22(self):
        words = ['the', 'quick', 'brown', 'fox']
        s = "thequickbrownfox"
        result = reconstruct_sentence(words, s)
        self.assertEqual(result, words)

        words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
        s = "bedbathandbeyond"
        result = reconstruct_sentence(words, s)
        expected = ['bed', 'bath', 'and', 'beyond']
        self.assertEqual(result, expected)

    def test_25(self):
        re = "ra."
        s = "ray"
        result = match_regex(re, s)
        self.assertTrue(result)

        re = ".*at"
        s = "chaaaaat"
        result = match_regex(re, s)
        self.assertTrue(result)

        re = "c*at"
        s = "at"
        result = match_regex(re, s)
        self.assertTrue(result)

        re = "cat.*"
        s = "catatemyfood!"
        result = match_regex(re, s)
        self.assertTrue(result)

        re = "cat*"
        s = "cats"
        result = match_regex(re, s)
        self.assertFalse(result)

    def test_26(self):
        four = LinkedListNode(4)
        three = LinkedListNode(3, four)
        two = LinkedListNode(2, three)
        head = LinkedListNode(1, two)

        remove_kth_last(3, head)
        self.assertEqual(head.next, three)

    def test_27(self):
        parens = "[{()[()]}]"
        result = is_well_formed(parens)
        self.assertTrue(result)

        parens = "([)]"
        result = is_well_formed(parens)
        self.assertFalse(result)

        parens = "((())"
        result = is_well_formed(parens)
        self.assertFalse(result)

        parens = "}{"
        result = is_well_formed(parens)
        self.assertFalse(result)

    def test_30(self):

        elev_map = [2, 1, 2]
        expected = 1
        result = rain_trapped(elev_map)
        self.assertEqual(result, expected)

        elev_map = [3, 0, 1, 3, 0, 5]
        expected = 8
        result = rain_trapped(elev_map)
        self.assertEqual(result, expected)

        elev_map = [3, 0, 1, 3, 0, 1, 0]
        expected = 6
        result = rain_trapped(elev_map)
        self.assertEqual(result, expected)

    def test_35(self):
        rgb = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
        result = sort_rgb(rgb)
        expected = ['R', 'R', 'R', 'G', 'G', 'B', 'B']
        self.assertEqual(result, expected)

        rgb = ['G', 'G', 'G']
        result = sort_rgb(rgb)
        expected = ['G', 'G', 'G']
        self.assertEqual(result, expected)

        rgb = []
        result = sort_rgb(rgb)
        expected = []
        self.assertEqual(result, expected)

        rgb = ['B', 'G', 'B']
        result = sort_rgb(rgb)
        expected = ['G', 'B', 'B']
        self.assertEqual(result, expected)
