class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ordered = []
        for i in range(len(speed)):
            ordered.append((position[i], (target - position[i])/speed[i]))
        ordered.sort()

        res = 0
        fleet = 0
        while ordered:
            time = ordered.pop()[1]
            if time > fleet:
                fleet = time
                res += 1
                  
        return res


        