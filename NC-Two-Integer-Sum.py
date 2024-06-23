# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # find difference between target and value. See if
        # stored in HashMap
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        # Alternate? Raises error for one test case
        # p1 = 0
        # p2 = len(nums) - 1

        # while p1 < p2:
        #     if nums[p1] + nums[p2] > target:
        #         p2 -= 1
        #     elif nums[p1] + nums[p2] < target:
        #         p1 += 1
        #     else:
        #         return [p1, p2]