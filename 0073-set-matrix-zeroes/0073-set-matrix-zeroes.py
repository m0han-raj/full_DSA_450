class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        zero_in_rows = [False]*rows
        zero_in_cols = [False]*cols

        for row_idx in range(rows):
            for col_idx in range(cols):
                if matrix[row_idx][col_idx]==0:
                    zero_in_rows[row_idx] = True
                    zero_in_cols[col_idx] = True

        for row_idx in range(rows):
            for col_idx in range(cols):
                if zero_in_rows[row_idx] or zero_in_cols[col_idx]:
                    matrix[row_idx][col_idx] = 0        