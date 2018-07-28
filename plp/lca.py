import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        lca = helper(root, p, q)
        return lca

def helper(cur, p, q):
    foundP = cur.val == p
    foundQ = cur.val == q

    if cur.left:
        valL = helper(cur.left, p, q)
        if valL == p:
            foundP = True
        elif valL == q:
            foundQ = True
        elif valL != None:
            return valL
    if cur.right:
        valR = helper(cur.right, p, q)
        if valR == p:
            foundP = True
        elif valR == q:
            foundQ = True
        elif valR != None:
            return valR

    if foundP and foundQ:
        return cur.val
    elif foundP:
        return p
    elif foundQ:
        return q
    else:
        return None

class TestLCA(unittest.TestCase):

    def test_simple(self):
        root = TreeNode(3)
        l = TreeNode(5)
        r = TreeNode(1)
        root.left = l
        root.right = r
        self.assertEqual(lowestCommonAncestor(root, 1, 5), 3)

    def test_complex(self):
        root = TreeNode(3)
        five = TreeNode(5)
        one = TreeNode(1)
        six = TreeNode(6)
        two = TreeNode(2)
        zero = TreeNode(0)
        eight = TreeNode(8)
        seven = TreeNode(7)
        four = TreeNode(4)
        root.left = five
        root.right = one
        five.left = six
        five.right = two
        one.left = zero
        one.right = eight
        two.left = seven
        two.right = four

        self.assertEqual(lowestCommonAncestor(root, 6, 4), 5)
