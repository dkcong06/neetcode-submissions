class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            cumsum = numbers[i] + numbers[j]
            if cumsum == target:
                return [i+1, j+1] 
            elif cumsum > target:
                j-=1
            else:
                i+=1
        