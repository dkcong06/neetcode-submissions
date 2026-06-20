class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minspeed = 0
        while l <= r:
            print(l, r)
            m = (l + r)//2
            time = 0
            for pile in piles:
                time += -(-pile//m)
            print(time)
            if time > h:
                l = m + 1
            else:
                if m < minspeed or minspeed == 0:
                    minspeed = m
                r = m - 1
        return minspeed
