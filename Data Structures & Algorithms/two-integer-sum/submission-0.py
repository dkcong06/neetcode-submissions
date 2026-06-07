class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i in range(len(nums)):
            if (target - nums[i]) in need:
                return [need[target - nums[i]] , i]
            if nums[i] not in need:
                need[nums[i]] = i