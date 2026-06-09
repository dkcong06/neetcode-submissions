class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long, count = 0, 0
        numset = set(nums)
        seenset = set()
        for num in nums:
            if num not in seenset:
                seenset.add(num)
                count = 1
                upper = lower = num
                while upper + 1 in numset:
                    upper += 1
                    seenset.add(num)
                    count += 1
                while lower - 1 in nums:
                    lower -= 1
                    seenset.add(num)
                    count +=1
                if count > long:
                    long = count
        return long
