class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key = k
        d = Dict.fromkeys(nums, 0)
        for num in nums:
            d[num] += 1
        
        freq = [[] for i in range(len(nums) + 1)]
        for k, v in d.items():
            freq[v].append(k)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == key:
                    return res