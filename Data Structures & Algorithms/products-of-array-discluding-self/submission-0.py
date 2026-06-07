class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        result = [0] * len(nums)

        for i in range(len(nums) - 1):
            left[i+1] = left[i] * nums[i]
            right[len(nums)-i-2] = right[len(nums)-i-1] * nums[len(nums)-i-1]
        
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        
        return result 

