# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely 
# filled, and all nodes in the last level are as far left as possible. It can have 
# between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Method: BFS
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                q.append(node.left)
                q.append(node.right)
            else:
                while q:
                    if q.popleft() is not None:
                        return False

        return True