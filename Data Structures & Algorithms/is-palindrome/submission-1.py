class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for c in s:
            if c != " " and (c.isalpha() or c in "1234567890"):
                ns += c.lower()
        if ns == ns[::-1]:
            return True
        else:
            return False