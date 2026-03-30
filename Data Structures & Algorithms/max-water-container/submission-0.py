class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_ar = 0
        while i < j:
            ar = min(heights[i], heights[j]) * (j - i)
            if ar > max_ar:
                max_ar = ar
            if heights[i] > heights[j]:
                j -= 1
            elif heights[j] > heights[i]:
                i += 1
            else:
                i += 1
        return max_ar
    
