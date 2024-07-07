# You are given an integer n representing 
# the number of steps to reach the top of 
# a staircase. You can climb with either 
# 1 or 2 steps at a time.

# Return the number of distinct ways to 
# climb to the top of the staircase.

class Solution:
    # bottom-up memoization
    # time O(n)
    def climbStairs(self, n: int) -> int:
        one, two, = 1, 1

        for i in range(n-1):
            temp = one
            one = one+two
            two = temp

        return one