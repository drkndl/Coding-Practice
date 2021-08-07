class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        i=1
        while i < len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                #print(l[i])
                i += 1
        return len(nums)
