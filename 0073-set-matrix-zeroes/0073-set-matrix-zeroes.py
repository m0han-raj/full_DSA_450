class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m , n =len(matrix) , len(matrix[0])
        rows = set()
        cols = set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:
                    rows.add(r)
                    cols.add(c)
        for r in range(m):
            for c in range(n):
                if r in rows or c in cols:
                    matrix[r][c]=0

        