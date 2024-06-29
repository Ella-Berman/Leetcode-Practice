# Given the root of a binary tree, return true if it is a valid 
# binary search tree, otherwise return false.

# A valid binary search tree satisfies the following constraints:
    # The left subtree of every node contains only nodes with keys 
        # less than the node's key.
    # The right subtree of every node contains only nodes with keys 
        # greater than the node's key.
    # Both the left and right subtrees are also binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # remember: all values need to work with the overall root
    # Time: O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # pass in the node and boundaries
        def valid(node, left, right):
            if not node:
                return True

            if not(node.val < right and node.val > left):
                return False
            # check if left and right subtrees are valid
            return (valid(node.left, left, node.val) and 
                valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))