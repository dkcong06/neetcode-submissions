class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if stack and temperatures[i] > stack[-1][0]:
                while stack and stack[-1][0] < temperatures[i]:
                    top = stack.pop()
                    res[top[1]] = i - top[1]
                stack.append((temperatures[i], i))
            else:
                stack.append((temperatures[i], i))
        return res
                     
            
