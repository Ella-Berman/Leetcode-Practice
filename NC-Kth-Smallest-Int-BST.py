# Given the root of a binary search tree, and an integer 
# k, return the kth smallest value (1-indexed) in the tree.

# A binary search tree satisfies the following constraints:

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
    # in order traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive solution:
        inOrder = []

        def trav(node):
            if not node:
                return

            trav(node.left)
            inOrder.append(node.val)
            trav(node.right)

        trav(root)

        return inOrder[k-1]

        # iterative solution:
        # n = 0
        # stack = []
        # cur = root # node currently visiting

        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left # find smallest val 

        #     cur = stack.pop()
        #     n += 1
        #     if n == k: # at least k nodes in tree
        #         return cur.val
        #     cur = cur.right