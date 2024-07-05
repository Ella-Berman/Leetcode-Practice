#Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# alternate: make array of bst inorder and use two pointers on that array
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.seen = set()

        # HELPER   
        def dfs(node):
            if not node:
                return False

            if k-node.val in self.seen:
                return True

            self.seen.add(node.val)

            return dfs(node.left) or dfs(node.right)

        return dfs(root)