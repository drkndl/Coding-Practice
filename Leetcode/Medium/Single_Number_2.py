# Runtime: 52 ms, faster than 82.54% of Python3 online submissions for Single Number II.
# Memory Usage: 16.2 MB, less than 7.17% of Python3 online submissions for Single Number II.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        d = dict(Counter(nums))
        for k,v in d.items():
            if v ==1:
                return k 
