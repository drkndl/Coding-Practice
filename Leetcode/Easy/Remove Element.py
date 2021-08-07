#Runtime: 32 ms, faster than 73.37% of Python3 online submissions for Remove Element.
#Memory Usage: 14.1 MB, less than 7.10% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while i < len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i=i+1
        return len(nums)
