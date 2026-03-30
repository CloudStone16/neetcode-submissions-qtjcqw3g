class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        j = 0
        k = len(nums) - 1
        result = []
        for i, e in enumerate(nums):
            j = i + 1
            if e > 0:
                break
            
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            else:
                while j < k:
                    target = - e
                    if nums[j] + nums[k] > target:
                        k -= 1
                    elif nums[j] + nums[k] < target:
                        j += 1
                    else:
                        result += [[nums[i], nums[j], nums[k]]]
                        j += 1
                        k -= 1
                        while nums[j] == nums[j - 1] and j < k:
                            j += 1
                        while nums[k] == nums[k] + 1:
                            k -= 1
                        print(result)
        return result
