# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn into set and find starts of sequences
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if start of sequence
            if (n - 1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest