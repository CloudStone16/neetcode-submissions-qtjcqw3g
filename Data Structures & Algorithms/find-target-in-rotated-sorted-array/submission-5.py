class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                # Left half is sorted
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    # Final search space
                    r = mid - 1

            elif nums[mid] <= nums[r]:
                # Right half is sorted
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: 
                    # Final Search Space
                    l = mid + 1


        return -1