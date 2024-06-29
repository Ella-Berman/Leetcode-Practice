# Given a binary tree root, return the level order 
# traversal of it as a nested list, where each sublist 
# contains the values of nodes at a particular level in 
# the tree, from left to right.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Method: BFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        if not root:
            return ret

        queue = deque()
        queue.append(root) # append to right of queue

        while queue:
            levelNodes = []
            # for each node in the queue
            for i in range(len(queue)):
                cur =  queue.popleft()
                if cur:
                    levelNodes.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right) 
            ret.append(levelNodes)   

        return ret