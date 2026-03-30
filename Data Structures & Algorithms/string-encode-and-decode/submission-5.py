class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word))
            s += "#"
            s += word
   
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        print(s)
        while i < len(s):
            if s[i].isnumeric():
                l = ""
                while s[i] != '#' and s[i].isnumeric():
                    l += s[i]
                    i += 1
                l = int(l)
                ts = ""
                for j in range(i + 1, l + i + 1):
                    ts += s[j]
                i += l
           
                strs.append(ts)
            i += 1
        return strs