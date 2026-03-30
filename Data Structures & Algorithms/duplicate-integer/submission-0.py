class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nl = []
        flag = False
        for ele in nums:
            if ele not in nl:
                nl.append(ele)
            else:
                flag = True
        return flag