# You are given a rectangular island heights where heights[r][c] 
# represents the height above sea level of the cell at coordinate 
# (r, c).

# The islands borders the Pacific Ocean from the top and left sides, 
# and borders the Atlantic Ocean from the bottom and right sides.

# Water can flow in four directions (up, down, left, or right) 
# from a cell to a neighboring cell with height equal or lower. 
# Water can also flow into the ocean from cells adjacent to the ocean.

# Find all cells where water can flow from that cell to both the 
# Pacific and Atlantic oceans. Return it as a 2D list where each 
# element is a list [r, c] representing the row and column of the 
# cell. You may return the answer in any order.

class Solution:
    # Matrix DFS
    # find all islands that can reach the pacific ocean.
    # find out which can reach the atlantic ocean.
    # from this, figure out which can reach both
    # O(n*m)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # visit sets

        # Helper dfs function
        def dfs(r, c, visit, prevHeight):
            # return if out of bounds or has greater height than prev
            if((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                    return

            visit.add((r, c))
            # run dfs on neighbors
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # dfs on top and bottom rows
        for c in range(COLS):
            # DFS on top row to see which can reach the pacific
            dfs(0, c, pac, heights[0][c])
            # DFS on bottowm row to see which can reach the atlantic
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        # dfs on left and right cols
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # add all positions that are in both the pac
        # and atl sets
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res