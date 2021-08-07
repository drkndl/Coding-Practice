import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1=nums1
        self.nums2=nums2
        for item in nums2:
            nums1.append(item)
        nums1.sort()
        if len(nums1)%2==0:
            med1=nums1[int(len(nums1)/2)-1]
            med2=nums1[int(len(nums1)/2)]
            median=(med1+med2)/2
        else:
            median=nums1[math.ceil(len(nums1)/2)-1]
        return median
#Runtime: 96 ms, faster than 79.49% of Python3 online submissions for Median of Two Sorted Arrays.
#Memory Usage: 14 MB, less than 63.72% of Python3 online submissions for Median of Two Sorted Arrays.
