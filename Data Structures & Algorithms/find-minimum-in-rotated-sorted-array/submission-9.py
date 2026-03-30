class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0
        mid = (l + r) // 2
        res = nums[mid]
        while l <= r:
            if nums[l] < nums[r]:
               res = min(nums[l], res)
               break 
            mid = (l + r) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[l]: 
                l = mid + 1
            else:
                r = mid - 1
        return res