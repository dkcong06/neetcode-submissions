class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = []
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        reps = list(count.values())
        reps.sort()
        kth = reps[len(reps) - k]
        for key, value in count.items():
            if value >= kth:
                top.append(key)
        return top
        
        
             




        