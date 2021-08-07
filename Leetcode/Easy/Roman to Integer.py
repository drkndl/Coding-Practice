#Runtime: 40 ms, faster than 92.98% of Python3 online submissions for Roman to Integer.
#Memory Usage: 14.2 MB, less than 5.10% of Python3 online submissions for Roman to Integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        integer=0
        roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        for letter in range(len(s)):
            integer = integer + roman[s[letter]]
            if letter>0:
                if roman[s[letter]]>roman[s[letter-1]]:
                    integer = integer - roman[s[letter]] - roman[s[letter-1]]
                    integer = integer + roman[s[letter]] - roman[s[letter-1]]
        return integer
