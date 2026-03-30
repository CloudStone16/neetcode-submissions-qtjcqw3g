class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lu = 0
        uu = len(matrix) - 1
        while lu <= uu:
            mu = (lu + uu) // 2
            u = len(matrix[mu]) - 1
            l = 0
            if matrix[mu][l] > target:
                uu = mu - 1
            elif matrix[mu][u] < target:
                lu = mu + 1
            else:
                while l <= u:
                    mid = (l + u) // 2
                    if matrix[mu][mid] > target:
                        u = mid - 1
                    elif matrix[mu][mid] < target:
                        l = mid + 1
                    else:
                        return True
                return False
        return False
        