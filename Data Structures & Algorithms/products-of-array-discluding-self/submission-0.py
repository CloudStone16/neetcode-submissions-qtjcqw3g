class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        prod = 1
        for i in range(len(nums)):
            pre.append(prod)
            prod = prod * nums[i]
        prod = 1
        print(pre)
        for j in range(len(nums)-1, -1, -1):
            suf.insert(0, prod)
            prod = prod * nums[j]
        print(suf)
        prods = []
        for k in range(len(nums)):
            prods.append(pre[k] * suf[k])
            
        return prods