class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            l = [0] * 26
            for char in s:
                l[ord(char) - ord("a")] += 1
            try:
                d[tuple(l)].append(s)
            except KeyError:
                d[tuple(l)] = [s]
        new_arr = []
        for keys in d:
            sub_arr = []
            for ele in d[keys]:
                sub_arr.append(ele)
                print(keys)
            new_arr.append(sub_arr)
        return new_arr