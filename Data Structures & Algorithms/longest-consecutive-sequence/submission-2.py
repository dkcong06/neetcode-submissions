class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = 0
        numset = set(nums)
        for num in numset:
            if num - 1 not in numset:
                len = 1
                while num + len in numset:
                    len += 1
                if len > long:
                    long = len
        return long
            

