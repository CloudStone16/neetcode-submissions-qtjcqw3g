class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        chars = {}
        maxc = 0

        while r < len(s):
            if s[r] in chars:
                chars[s[r]] += 1
            else:
                chars[s[r]] = 1

            if chars[s[r]] > maxc:
                maxc = chars[s[r]]
            
            while k < ((r - l + 1) - maxc):
                chars[s[l]] -= 1
                l = l + 1
                
            res = max(res, (r - l + 1))
            r = r + 1
        return res
