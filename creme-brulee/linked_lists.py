import unittest

# Linked List definition
class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# 2.4. Partition. Partition a linked list around value x, such that values
# less than x come before values greater than or eq to x
def partition(head, x):
    part = LinkedList(None, head)
    curr = part
    while curr and curr.next:
        if curr.next.val < x:

            to_swap = curr.next
            curr.next = curr.next.next
            nn = part.next

            part.next = to_swap
            to_swap.next = nn
            part = to_swap

        else:
            curr = curr.next
    return

# 2.6. Palindrome. Check if a linked list is a palindrome
def is_palindrome(head):
    curr = head
    reversed = []
    while curr:
        reversed.append(curr.val)
        curr = curr.next
    curr = head
    while curr:
        curr_rev = reversed.pop()
        if curr.val != curr_rev:
            return False
        curr = curr.next
    return True

# 2.7. Intersection. Given two singly linked lists, determine if they intersect
def intersection(l1, l2):
    # determine lengths of two lists
    l1_len = 0
    curr = l1
    while curr:
        l1_len += 1
        curr = curr.next

    l2_len = 0
    curr = l2
    while curr:
        l2_len += 1
        curr = curr.next

    # offset one start so that lists are the same length
    offset = l1_len - l2_len
    curr1, curr2 = l1, l2
    if offset > 0:
        while offset > 0:
            curr1 = curr1.next
            offset -= 1
    elif offset < 0:
        while offset < 0:
            curr2 = curr2.next
            offset += 1

    while curr1:
        if curr1 is curr2:
            return True
        curr1, curr2 = curr1.next, curr2.next
    return False

# 2.8. Loop detection
# Given a circular linked list, implement an algorithm that returns the node at
# the beginning of the loop
def detect_loop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return slow

class TestLinkedList(unittest.TestCase):

    def test_partition(self):
        h = LinkedList(4)
        g = LinkedList(1, h)
        f = LinkedList(2, g)
        e = LinkedList(5, f)
        d = LinkedList(11, e)
        c = LinkedList(8, d)
        b = LinkedList(5, c)
        a = LinkedList(3, b)

        partition(a, 5)
        lower = set()
        higher = set()
        curr = a
        count = 0
        while curr:
            # print(curr.val)
            if count < 4:
                lower.add(curr.val)
            else:
                higher.add(curr.val)
            count += 1
            curr = curr.next
            if count > 7:
                break
        self.assertEqual({1, 2, 3, 4}, lower)
        self.assertEqual({5, 8, 11}, higher)

    def test_palindrome(self):
        e = LinkedList("a")
        d = LinkedList("b", e)
        c = LinkedList("c", d)
        b = LinkedList("b", c)
        a = LinkedList("a", b)
        result = is_palindrome(a)
        self.assertTrue(result)

        e = LinkedList("e")
        d = LinkedList("b", e)
        c = LinkedList("c", d)
        b = LinkedList("b", c)
        a = LinkedList("a", b)
        result = is_palindrome(a)
        self.assertFalse(result)

    def test_intersection(self):
        e = LinkedList("e")
        d = LinkedList("d", e)

        c1 = LinkedList("c", d)
        b1 = LinkedList("b", c1)
        a1 = LinkedList("a", b1)

        b2 = LinkedList("b", d)
        a2 = LinkedList("a", b2)
        result = intersection(a1, a2)
        self.assertTrue(result)

        c1 = LinkedList("c")
        b1 = LinkedList("b", c1)
        a1 = LinkedList("a", b1)

        b2 = LinkedList("b")
        a2 = LinkedList("a", b2)
        result = intersection(a1, a2)
        self.assertFalse(result)

    def test_detect_loop(self):

        e = LinkedList("e")
        d = LinkedList("d", e)
        c = LinkedList("c", d)
        b = LinkedList("b", c)
        a = LinkedList("a", b)
        e.next = c

        expected = c
        result = detect_loop(a)
        self.assertEqual(result, expected)

        e.next = None
        expected = None
        result = detect_loop(a)
        self.assertEqual(result, expected)
