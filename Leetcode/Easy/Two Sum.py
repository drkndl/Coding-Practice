class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums=nums
        self.target=target
        for i in range(len(self.nums)):
            if self.target-self.nums[i] in self.nums and i!=self.nums.index(self.target-self.nums[i]):
                k=nums.index(self.target-self.nums[i])
                return [i, k]
        
