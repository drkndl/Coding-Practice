# Runtime: 36 ms, faster than 53.41% of Python3 online submissions for First Missing Positive.
# Memory Usage: 14.3 MB, less than 8.73% of Python3 online submissions for First Missing Positive.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1, 2**31):
            if i not in nums:
                return i
