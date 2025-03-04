class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        v= nums[::-1]

        for n in range(1, len(nums)):
            nums[n] *= nums[n-1] or 1
            v[n] *= v[n-1] or 1

        return max(nums + v) 
        