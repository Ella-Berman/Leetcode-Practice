# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
  #def hasDuplicate(self, nums: List[int]) -> bool:
  def hasDuplicate(self, nums):
    d = {}
    for num in nums:
        if d.get(num) is not None:
            return True
        else:
            d[num] = 1
          
    return False
    
      # d = {}
      # for num in nums:
      #     if d.get(num) is not None:
      #         d[num] = d[num] + 1
      #     else:
      #         d[num] = 1

      # for key, val in d.items():
      #     if val > 1:
      #         return True
      # return False

# ALTERNATE:
# - sort list and set neighbor pointers. If neighbors same, then true (O(nlogn), O(1))
# - hashset, can add vals and check if they already exist (O(n), O(n))