# Given the root of a binary tree, write a function that returns True if the value of root is equal to the sum of the values of all its descendants. Return False otherwise.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def check_root_sum(root):
  if not root:
    return True
    
  return root == find_sum(root.left) + find_sum(root.right)

# Helper
def find_sum(node):
  if not node:
    return 0

  return node.val + find_sum(node.left) + find_sum(node.right)

