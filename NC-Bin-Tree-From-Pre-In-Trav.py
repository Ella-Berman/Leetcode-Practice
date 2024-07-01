# You are given two integer arrays preorder and inorder.

# preorder is the preorder traversal of a binary tree
# inorder is the inorder traversal of the same tree
# Both arrays are of the same size and consist of unique values.
# Rebuild the binary tree from the preorder and inorder traversals 
# and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive solution
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # overall root is always first val in preorder
        root = TreeNode(preorder[0])
        # find position of the root in the inorder lst
        mid = inorder.index(preorder[0])
        # build left subtree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # build right subtree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root