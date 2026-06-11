class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        rain, barrier = 0, 0
        top = max(height)
        while l+1 < len(height)-1 and height[l+1] >= height[l]:
            l+=1
        barrier = l
        while r > 0 and height[r-1] >= height[r]:
            r-=1
        while height[l] < top:
            if height[l+1] < height[barrier]:
                rain += height[barrier] - height[l+1]
            else:
                barrier = l+1
            l+=1
        barrier = r
        while l < r:
            if height[r-1] < height[barrier]:
                rain += height[barrier] - height[r-1]
            else:
                barrier = r-1
            r-=1
        return rain

