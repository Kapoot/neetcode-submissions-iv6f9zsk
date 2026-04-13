class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        L = 0
        R = 0

        while R < len(prices):
            while prices[L] > prices[R]:
                L += 1
            else:
                max_profit = max(max_profit, prices[R] - prices[L])
                R += 1
        
        return max_profit
            
        

        