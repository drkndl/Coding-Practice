#Runtime: 36 ms, faster than 61.24% of Python3 online submissions for Merge Sorted Array.
#Memory Usage: 14.1 MB, less than 55.96% of Python3 online submissions for Merge Sorted Array.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
