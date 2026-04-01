class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        for row in matrix:
            # Perform binary search only if the target is within the row range
            if row[0] <= target <= row[-1]:
                l, r = 0, len(row) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
        return False