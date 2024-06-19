# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

class Solution:
  # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    def canPlaceFlowers(self, flowerbed, n):
      count = 0

      for i in range(len(flowerbed)):

          # Check if the current plot is empty
          if flowerbed[i] == 0:

              # Check the previous and next plot, considering the edge cases
              prev_empty = i == 0 or flowerbed[i - 1] == 0
              next_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

              # If both adjacent plots are empty, plant a flower here
              if prev_empty and next_empty:
                  flowerbed[i] = 1  # Mark this plot as planted
                  count += 1  # Increment the count of flowers that can be planted

              # If we've planted enough flowers, return true immediately
              if count >= n:
                  return True

      return count >= n


# ALTERNATE SOLUTION:

def canPlaceFlowers2(self, flowerbed, n):
    fb = [0] + flowerbed + [0]

    for i in range(1, len(fb) - 1):
        if fb[i-1] == 0 and fb[i] == 0 and fb[i+1] == 0:
            fb[i] = 1
            n -= 1
            
    return n <= 0
            