class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        most = 0
        while i < j:
            size = (j-i) * min(heights[i], heights[j])
            if size > most:
                most = size
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return most 
