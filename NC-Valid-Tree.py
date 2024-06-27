# Given n nodes labeled from 0 to n - 1 and a list of 
# undirected edges (each edge is a pair of nodes), write a 
# function to check whether these edges make up a valid tree.
# (valid trees are connected and have no loops)
class Solution:
    # Time and Mem = O(E+V)
    # create an adjacency list of neighbors for each node
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        # for each node, create pair in hashmap w
        # val for node and list of connections
        adj = { i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        # can detect loops
        def dfs(i, prev):
            # loop detected
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                # recursive call
                if not dfs(j, i):
                    return False
            return True

        # check connected
        return dfs(0, -1) and n == len(visit)