#Runtime: 48 ms, faster than 61.51% of Python3 online submissions for Search Insert Position.
#Memory Usage: 15.1 MB, less than 5.01% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for item in range(len(nums)):
            if nums[item]==target:
                return item
            
        for item in range(len(nums)-1):
            if target>nums[item] and target<nums[item+1]:
                return item+1
            
        if target>max(nums):
            return len(nums)
        else:
            return 0
            
