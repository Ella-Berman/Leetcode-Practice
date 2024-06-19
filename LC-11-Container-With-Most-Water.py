# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
  # def maxArea(self, height: List[int]) -> int:
  def maxArea(self, height):
      # Create largest range, by creating a left and right pointer
      l, r = 0, len(height) - 1
      maxArea = 0

      # At every part of the range calculate the current area at this width and check against our max area
      while l < r:
          width = r - l
          minHeight = min(height[l], height[r])
          currArea = minHeight * width
          maxArea = max(maxArea, currArea)

          # Reduce the range/width while maintaining the maximum height 
          if height[l] < height[r]:
              l += 1
          else:
              r -= 1

      # Return max area found
      return maxArea