# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your
# profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Buy
        right = 1  # Sell
        min_price = 9999999999
        n = len(prices)

        for price in prices:
            if price < min_price:
                min_price = price

        max_after_min = -99999999
        for index, price in enumerate(prices):
            if price == min_price:
                for j in range(index + 1, n):
                    if prices[j] > max_after_min:
                        max_after_min = prices[j]

        return max_after_min - min_price


if __name__ == "__main__":
    prices_list = [7,1,5,3,6,4]
    obj = Solution()
    print(obj.maxProfit(prices_list))
