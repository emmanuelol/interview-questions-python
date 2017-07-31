import unittest

def is_bst(root):
    """ Given the root of a binary tree, return true if it is a binary search tree. """
    pass


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tests(unittest.TestCase):

    def create_bst_1(self):
        return Node(5, Node(3, Node(1), Node(9)), Node(6))

    def create_bst_2(self):
        return Node(5, Node(3, Node(1), Node(4)), Node(7, Node(6), Node(8)))

    def test_is_bst(self):
        self.assertFalse(is_bst(self.create_bst_1()))
        self.assertTrue(is_bst(self.create_bst_2()))



if __name__ == '__main__':
    unittest.main()
