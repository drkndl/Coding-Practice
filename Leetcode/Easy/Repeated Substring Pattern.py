#Runtime: 40 ms, faster than 72.11% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 14.3 MB, less than 6.53% of Python3 online submissions for Repeated Substring Pattern.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1,n//2+1):
            if not n%i and s== n//i*s[:i]:              
                return True        
        return False
