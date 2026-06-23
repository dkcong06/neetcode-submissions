class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value, timestamp)]
        return None         

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or self.map[key][0][1] > timestamp:
            return ""
        else: 
            l,r = 0, len(self.map[key])-1
            while l <= r:
                m = (l+r)//2
                if self.map[key][m][1] > timestamp:
                    r = m-1
                elif self.map[key][m][1] < timestamp: 
                    if len(self.map[key]) == m+1 or self.map[key][m+1][1] > timestamp:
                        return self.map[key][m][0]
                    else:
                        l = m+1
                else:
                    return self.map[key][m][0]
                    

