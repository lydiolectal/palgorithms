import unittest

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
    for i, num in enumerate(arr):
        if num <= length:
            temp = arr[num - 1]
            arr[num - 1] = num
            arr[i] = temp

    for i, num in enumerate(arr):
        if num != i + 1:
            return i + 1

    return length


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

    def test_4(self):
        arr = [3, 4, 1, -1]
        result = first_missing_int(arr)
        expected = 2
        self.assertEqual(result, expected)

        arr = [1, 2, 0]
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
