class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        if (n == 1):
            return a
        elif (n == 2):
            return b
        else:
            for i in range(n-2):
                c = a + b
                a = b
                b = c
            return b
        
        