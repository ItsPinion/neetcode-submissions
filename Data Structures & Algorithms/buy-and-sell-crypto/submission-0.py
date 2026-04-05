class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left: int = 0
        right: int = 1

        profit: int = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = max(prices[right] - prices[left], profit)

            else:
                left = right
            right += 1

        return profit

