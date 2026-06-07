class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        rolling = 1
        for i in range(len(nums)-1):
            result[i+1] = result[i] * nums[i]
        
        for i in range(len(nums)-1):
            rolling *= nums[len(nums)-i-1]
            result[len(nums)-i-2] *= rolling 

        return result
