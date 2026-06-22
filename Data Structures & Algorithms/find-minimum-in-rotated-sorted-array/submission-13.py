class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1   
        mini = nums[0]     
        while l <= r:
            print(l, r)
            if nums[(l + r)//2] > mini:
                l = (l + r)//2 + 1
            elif nums[(l + r)//2] <= mini:
                if(nums[(l+r)//2 - 1] > nums[(l+r)//2]):
                    return nums[(l+r)//2]
                
                mini = nums[(l+r)//2 - 1]
                r = (l + r)//2 - 1
            print(l, r)
        return mini


        