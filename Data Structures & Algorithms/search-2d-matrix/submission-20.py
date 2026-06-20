class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l < r:
            m = l + (r - l)//2
            print(l, m, r)
            if matrix[m][0] == target: 
                return True
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] < target: 
                if l == m:
                    if matrix[m+1][0] <= target:
                        l = l + 1
                    break
                l = m
        print(l)
        ll, rr = 0, len(matrix[l]) - 1
        while ll <= rr:
            m = ll + (rr - ll)//2 
            print(ll, m, rr)
            if matrix[l][m] == target:
                return True
            elif matrix[l][m] > target:
                rr = m - 1
            elif matrix[l][m] < target:
                ll = m + 1
        return False 

