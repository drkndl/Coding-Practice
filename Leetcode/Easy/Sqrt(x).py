#Runtime: 108 ms, faster than 11.94% of Python3 online submissions for Sqrt(x).
#Memory Usage: 30.7 MB, less than 8.54% of Python3 online submissions for Sqrt(x).

import numpy as np
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(np.sqrt(x))
