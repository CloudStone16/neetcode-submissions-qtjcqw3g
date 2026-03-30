class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for i, c in count.items():
            freq[c].append(i)
        result = []
        for i in range(len(freq) - 1, 0, -1):
            if freq[i]:
                for num in freq[i]:
                    result.append(num)
                if len(result) == k:
                    return result
