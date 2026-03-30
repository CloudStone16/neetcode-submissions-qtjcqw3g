class Solution:
    def isPalindrome(self, s: str) -> bool:
        size = len(s)
        i = 0
        j = size - 1
        flag = True
        while i <= j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    flag = False
                    
                    break
                print(i, j)
                i += 1
                j -= 1
            else:
                if not s[i].isalnum():
                    i+=1
                if not s[j].isalnum():
                    j -= 1
        return flag
