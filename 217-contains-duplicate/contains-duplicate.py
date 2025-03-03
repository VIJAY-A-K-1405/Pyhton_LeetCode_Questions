# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False

from collections import Counter
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
