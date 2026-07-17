class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])

        heap =[]

        for r in range(n):
            heapq.heappush(heap , (matrix[r][0],r,0))

        for _ in range(k-1):

            value , row, col = heapq.heappop(heap)

            if col+1 < m :
                heapq.heappush(heap , (matrix[row][col+1] , row , col+1))

        return heapq.heappop(heap)[0]