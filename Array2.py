class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0;
        sub_profit = 0;
        if len(prices) == 0 or len(prices) == 1:
            return 0
        for i in range(1,len(prices)):
            if prices[i] < prices[i-1]:
                continue
            elif prices[i] > prices[i-1]:
                sub_profit = prices[i] - prices[i-1]
                profit += sub_profit
            elif prices[i] == prices[i-1]:
                continue
        return profit
