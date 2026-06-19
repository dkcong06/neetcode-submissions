class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxi = 0
        for i in range(len(heights)):
            height, index = 0, i
            while stack and stack[-1][0] > heights[i]:
                height, index = stack.pop()
                area = (i - index)*height
                if area > maxi: 
                    maxi = area
                    print(maxi)
            stack.append((heights[i], index))
        while stack:
            height, index = stack.pop()
            area = (len(heights) - index)*height
            if area > maxi:
                maxi = area
        return maxi


        


        