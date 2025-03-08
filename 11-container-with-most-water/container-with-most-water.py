class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) -1 
        max_wt = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            max_wt = max(max_wt, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_wt


        