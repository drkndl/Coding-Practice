#Runtime: 240 ms, faster than 55.19% of Python3 online submissions for Sum of Square Numbers.
#Memory Usage: 14.2 MB, less than 46.69% of Python3 online submissions for Sum of Square Numbers.

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(c):
            other = c - i*i
            if other<0:
                return False
            if math.sqrt(other)==math.isqrt(other):
                return True
        return True
