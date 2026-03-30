class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers) - 1
        j = len(numbers) - 1
        arr = []
        while i <= n and j >= 0:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] == target:
                arr.append(i + 1)
                arr.append(j + 1)
                return arr