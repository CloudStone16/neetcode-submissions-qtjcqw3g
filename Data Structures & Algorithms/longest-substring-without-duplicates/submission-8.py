class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        chars = set()
        res = 0
        size = 0
        for j in range(len(s)):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            chars.add(s[j])
            size = j - i + 1
            res = max(size, res)
        return res