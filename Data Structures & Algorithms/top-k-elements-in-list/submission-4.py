class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, val in count.items():
            freq[val].append(key)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            if freq[i] != []:
                for num in freq[i]:
                    result.append(num)
            if len(result) >= k:
                return result
        

        
             




        