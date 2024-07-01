# You are given an integer array prices where prices[i] is 
# the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a 
# different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose 
# to not make any transactions, in which case the profit would be 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP


        # # ALTERNATE:
        # # resulting max profit
        # res = 0

        # # lowest buying price
        # lowest = prices[0]

        # for price in prices:
        #     if price < lowest:
        #         lowest = price
        #     res = max(res, price-lowest)

        # return res