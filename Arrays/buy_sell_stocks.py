"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = 0
        diff = 0

        for nextDay in range(1, len(prices)):
            if prices[nextDay] - prices[current] < 0:
                current = nextDay
            if prices[nextDay] - prices[current] > diff:
                diff = prices[nextDay] - prices[current]
        return diff
