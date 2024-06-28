# Given a binary search tree (BST) where all node values 
# are unique, and two nodes from the tree p and q, return 
# the lowest common ancestor (LCA) of the two nodes.

# The lowest common ancestor between two nodes p and q is 
# the lowest node in a tree T such that both p and q as 
# descendants. The ancestor is allowed to be a descendant of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        # if p and q in separate subtrees, where split occurs is the
        # LCA
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root