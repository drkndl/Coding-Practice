# Runtime: 3492 ms, faster than 5.01% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.7 MB, less than 26.91% of Python3 online submissions for Find the Duplicate Number.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)>1:
                return i
