class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        soln_arr = []
        while lower <= upper:
            mid = (lower + upper) // 2
            s = self.calcEatingSpeed(piles, mid)
            if s > h:
                lower = mid + 1
            elif s <= h:
                soln_arr.append(mid)
                upper = mid - 1
        return min(soln_arr)
                
            
    def calcEatingSpeed(self, piles, rate):
        hours = 0
        for p in piles:
            res = (p + rate - 1) // rate
            hours += res
        return hours