# You are given an array prerequisites where prerequisites[i] = [a, b] 
# indicates that you must take course b first if you want to take 
# course a.

# For example, the pair [0, 1], indicates that to take course 0 you 
# have to first take course 1.
# There are a total of numCourses courses you are 
# required to take, labeled from 0 to numCourses - 1.

# Return true if it is possible to finish all courses, otherwise 
# return false.

class Solution:
    # Method: adjacency list 
    # O(n + p) = nodes + prereqs
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # for each course, we have a list of prereqs
        # for every course initially, map it to empty list
        preMap = {i: [] for i in range(numCourses)}
        visitSet = set() # all courses along cur DFS path

        # map courses to list of prereqs
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # dfs to determine whether crs can be completed
        def dfs(crs):
            # visiting course twice, so there is a cycle
            if crs in visitSet:
                return False
            # course has no prereqs, so can be completed
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            # run dfs on its prereqs
            for pre in preMap[crs]:
                if not dfs(pre): # if dfs(pre) is false, then false
                    return False

            visitSet.remove(crs)
            preMap[crs] = [] # indicates crs can be completed
            return True
            # end helper

        # run dfs on all courses (bc what if graph not fully
        # connected)
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True