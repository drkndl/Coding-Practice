# Runtime: 3584 ms, faster than 8.17% of Python3 online submissions for Single Number.
# Memory Usage: 16.7 MB, less than 22.54% of Python3 online submissions for Single Number.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i)==1:
                return i
