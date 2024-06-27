# Given a node in a connected undirected graph, return a deep 
# copy of the graph.

# Each node in the graph contains an integer value and a 
# list of its neighbors.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time: O(E+V)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        # depth first search to create a clone of node
        # and neighbors
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            # map old node to the copy
            oldToNew[node] = copy
            for nei in node.neighbors:
               copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None