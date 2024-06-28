# There is an undirected graph with n nodes. There is 
# also an edges array, where edges[i] = [a, b] means that 
# there is an edge between node a and node b in the graph.

# Return the total number of connected components in that graph.

class Solution:
    # Union find algorithm
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        # find root parent for a given node
        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]] # path compression
                res = parent[res]
            return res

        # performs a union, if applicable
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return 0

            # if p2 has more connections, it becomes parent of p1
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            # if p1 has more connections, it becomes parent of p2
            else:
                parent[p2] = p1
                rank[p2] += rank[p1]
            return 1 # if successful union

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res