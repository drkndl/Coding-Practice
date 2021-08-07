#Runtime: 408 ms, faster than 5.01% of Python3 online submissions for Squares of a Sorted Array.
#Memory Usage: 32.6 MB, less than 14.77% of Python3 online submissions for Squares of a Sorted Array.

import numpy as np
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        a=np.array(A)
        return sorted(a*a)
