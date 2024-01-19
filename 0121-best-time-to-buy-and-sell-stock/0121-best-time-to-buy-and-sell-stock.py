class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        min_p = prices[0]
        max_p = 0

        for price in prices:
            # Update the minimum price
            min_p = min(min_p, price)

            # Calculate the potential profit if selling at the current price
            p_p = price - min_p

            # Update the maximum profit if the potential profit is greater
            max_p = max(max_p, p_p)

        return max_p
