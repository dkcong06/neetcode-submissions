class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if nums[i] == nums[i-1] and i != 0:
                continue
            j,k = i+1, len(nums)-1
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j<len(nums)-1 and nums[j] == nums[j+1]:
                        j+=1
                    j+=1
                elif target < 0:
                    j+=1
                else:
                    k-=1
        return res


        