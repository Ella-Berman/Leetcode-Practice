# You are given a list of integers prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example #1:
# Input: prices = [7,1,5,3,6,4]
# Expected Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example #2:
# Input: prices = [7,6,4,3,1]
# Expected Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Method: single pass through array
#def maxProfit(self, prices: List[int]) -> int:
def max_profit(prices):
  # Initialize variables
  min_price = float('inf')
  max_profit = 0

  # Iterate through each price in the array
  for price in prices:
      # Update the minimum price seen so far
      min_price = min(min_price, price)
      # Calculate the potential profit
      current_profit = price - min_price
      # Update the maximum profit seen so far
      max_profit = max(max_profit, current_profit)

  return max_profit

      