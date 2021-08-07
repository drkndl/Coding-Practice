#Runtime: 32 ms, faster than 66.34% of Python3 online submissions for Implement strStr().
#Memory Usage: 14.3 MB, less than 12.15% of Python3 online submissions for Implement strStr().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1
