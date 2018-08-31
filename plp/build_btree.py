import unittest

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __eq__(self, other):
        l_equal, r_equal, v_equal = False, False, False
        if other:
            v_equal = self.val == other.val
            if not(self.left or other.left) or (self.left and other.left):
                l_equal = self.left == other.left
            if not(self.right or other.right) or (self.right and other.right):
                r_equal = self.right == other.right
        print(v_equal, l_equal, r_equal)
        return l_equal and r_equal and v_equal


def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if len(preorder) == 0 or len(inorder) == 0:
        return None

    root = preorder[0]
    inorder_map = dict(map(lambda x: (x[1], x[0]), enumerate(inorder)))
    inorder_root_idx = inorder_map[root]


class TestBuildTree(unittest.TestCase):
    def test_empty(self):
        preorder = []
        inorder = []

        self.assertEqual(buildTree(preorder, inorder), None)

    def test(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        
        rightSubtree = TreeNode(20)
        rightSubtree.left = TreeNode(15)
        rightSubtree.right = TreeNode(7)

        leftSubtree = TreeNode(9)

        expected = TreeNode(3)
        expected.left = leftSubtree
        expected.right = rightSubtree

        self.assertEqual(buildTree(preorder, inorder), expected)
    
    def test_eq(self):
        t1 = TreeNode(20)
        t2 = TreeNode(20)

        self.assertEqual(t1, t2)

    