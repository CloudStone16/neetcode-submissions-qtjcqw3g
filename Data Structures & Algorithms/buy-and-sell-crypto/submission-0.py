class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            p = prices[r] - prices[l]
            if p > 0:
                if p > maxP:
                    maxP = p
                r += 1
            else:
                l = r
                r += 1
        
        return maxP