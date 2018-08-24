import unittest

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

def addTwoNumbers(l1, l2):
    head = Node(0)
    sum_l = head
    carry = 0
    next_l = (l1, l2)
    while True:
        l1, l2 = next_l
        cur_sum, carry = get_sum(l1, l2, carry)
        sum_l.val = cur_sum
        next_l = get_next(l1, l2, carry)
        if not next_l:
            break
        new_node = Node(0)
        sum_l.next = new_node
        sum_l = new_node
    return head

def get_next(l1, l2, carry):
    next_l1, next_l2 = None, None
    if l1:
        next_l1 = l1.next
    if l2:
        next_l2 = l2.next
    if next_l1 or next_l2 or carry:
        return (next_l1, next_l2)
    return None

def get_sum(l1, l2, carry):
    d1 = l1.val if l1 else 0
    d2 = l2.val if l2 else 0
    carry, s = divmod(d1 + d2 + carry, 10)
    return (s, carry)

class TestLinkedList(unittest.TestCase):

    def test_add_no_carry(self):
        l1d3 = Node(3)
        l1d2 = Node(4)
        l1d1 = Node(2)
        l1d1.next = l1d2
        l1d2.next = l1d3

        l2d3 = Node(4)
        l2d2 = Node(6)
        l2d1 = Node(5)
        l2d1.next = l2d2
        l2d2.next = l2d3

        linked_sum = addTwoNumbers(l1d1, l2d1)
        self.assertEqual(linked_sum.val, 7)
        self.assertEqual(linked_sum.next.val,  0)
        self.assertEqual(linked_sum.next.next.val,  8)
