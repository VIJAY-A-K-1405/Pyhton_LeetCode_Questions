class Solution:
    def rob(self, nums: List[int]) -> int:
        ro1, ro2 = 0, 0 

        for n in nums:
            temp = max(ro1 + n, ro2)
            ro1 = ro2
            ro2 = temp
        return ro2
        