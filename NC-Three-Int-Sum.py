class Solution:
  # sort array, one loop for first val,
  # one loop for two-sum.
  # Time: O(nlogn) + O(n^2) = O(n^2)
  # Space: 1 or n depending on sort alg
  def threeSum(self, nums: List[int]) -> List[List[int]]:
      res = []
      nums.sort()

      # outer loop: choose first val
      for i, val in enumerate(nums):
          if val > 0:
              break
          # skip repeated first vals
          if i > 0 and val == nums[i - 1]:
              continue

          l, r = i + 1, len(nums) - 1
          # inner loop: two-sum approach
          while l < r:
              threeSum = val + nums[l] + nums[r]
              if threeSum > 0:
                  r -= 1
              elif threeSum < 0:
                  l += 1
              else:
                  res.append([val, nums[l], nums[r]])
                  l += 1
                  r -= 1
                  # only need to update one pointer. while
                  # loop conditions update the others.
                  while nums[l] == nums[l - 1] and l < r:
                      l += 1
      return res