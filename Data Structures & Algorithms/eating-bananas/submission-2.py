class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        mini = upper
        while lower <= upper:
            mid = (lower + upper) // 2
            s = self.calcEatingSpeed(piles, mid)
            if s > h:
                lower = mid + 1
            elif s <= h:
                if mid < mini:
                    mini = mid
                upper = mid - 1
        return mini
                
            
    def calcEatingSpeed(self, piles, rate):
        hours = 0
        for p in piles:
            res = (p + rate - 1) // rate
            hours += res
        return hours