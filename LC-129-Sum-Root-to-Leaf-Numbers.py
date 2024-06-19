# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def sumNumbers(self, root):
        return dfs(root, 0)

# Recursive depth first search helper function
def dfs(node, cur_num):
    if not node:
        return 0
        
    # calculate current number of path so far
    cur_num = cur_num * 10 + node.val

    # if the node is a leaf, return the number
    if not node.left and not node.right:
        return cur_num

    # return the sum of the recursive call on the left and right
    # children
    return dfs(node.left, cur_num) + dfs(node.right, cur_num)


# Time Complexity: O(N) because we need to visit each node once.
# Space Complexity: O(H) where H is the height of the tree, representing the space on the call stack due to recursion.
