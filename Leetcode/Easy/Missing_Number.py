# Runtime: 2392 ms, faster than 12.19% of Python3 online submissions for Missing Number.
# Memory Usage: 15.5 MB, less than 18.32% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(10**4):
            if i not in nums:
                return i
