# You are given an integer array nums where
# nums[i] represents the amount of money the 
# ith house has. The houses are arranged in a
# straight line, i.e. the ith house is the 
# neighbor of the (i-1)th and (i+1)th house.

# You are planning to rob money from the 
# houses, but you cannot rob two adjacent 
# houses because the security system will 
# automatically alert the police if two 
# adjacent houses were both broken into.

# Return the maximum amount of money you c
# an rob without alerting the police.
class Solution:
    # 1-d dp
    # recurrance: max(arr[0] + rob[2:n], rob[1:n])
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2