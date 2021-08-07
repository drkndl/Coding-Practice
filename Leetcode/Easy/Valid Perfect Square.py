#Runtime: 36 ms, faster than 21.14% of Python3 online submissions for Valid Perfect Square.
#Memory Usage: 14.3 MB, less than 7.63% of Python3 online submissions for Valid Perfect Square.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        dec_num = num**0.5 - int(num**0.5)
        if dec_num==0:
            return True
        else:
            return False
