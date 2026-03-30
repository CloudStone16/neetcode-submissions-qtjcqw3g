class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       ns = set(nums)
       c = 1
       max_c = 0
       start = None
       for num in nums:
            if num - 1 not in ns:
                checker = num
                while checker + 1 in ns:
                    c += 1
                    checker += 1
                if max_c < c:
                    max_c = c
            c = 1
       return max_c

