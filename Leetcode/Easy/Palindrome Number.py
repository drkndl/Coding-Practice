class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==''.join(reversed(str(x)))
#Runtime: 76 ms, faster than 47.52% of Python3 online submissions for Palindrome Number.
#Memory Usage: 13.9 MB, less than 41.53% of Python3 online submissions for Palindrome Number.
