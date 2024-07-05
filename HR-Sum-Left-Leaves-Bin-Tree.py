#Given the root of a binary tree, return the sum of all left leaves. A leaf is a node with no children.

#A left leaf is a leaf that is the left child of another node. As such, a tree with only one node has no left leaves.

# Example Input Tree
# 3
# / \
# 9 20
# / \
# 15 7
# Input: root = 3
# Expected Output: 24

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        self.total=0

        def dfs(node,left):
            if not node:
                return 

            dfs(node.left, True)
            dfs(node.right, False)

            # if left leaf
            if not node.left and not node.right and left:
                self.total += node.val

        dfs(root,False)

        return self.total



