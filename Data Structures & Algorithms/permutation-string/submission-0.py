class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash1 = [0] * 27
        hash2 = [0] * 27
        for ch in s1:
            hash1[ord(ch) - ord('a')] += 1
        l, r = 0, len(s1)
        for i in range(0, len(s1)):
            hash2[ord(s2[i]) - ord('a')] += 1

        if hash1 == hash2:
            return True



        while r < len(s2):
            hash2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            hash2[ord(s2[r]) - ord('a')] += 1
            r += 1
            if hash1 == hash2:
                return True
        
        return False
