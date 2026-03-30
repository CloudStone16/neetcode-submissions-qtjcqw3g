class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(1, len(height) - 1):
            pre = max(height[:i])
            suf = max(height[i::])

            amount = min(pre, suf) - height[i] 
            amount = 0 if amount < 0 else amount
            print(amount)
            total += amount
        return total
