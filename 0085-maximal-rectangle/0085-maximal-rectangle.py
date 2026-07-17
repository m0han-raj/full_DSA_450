from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largestRectangleArea(heights: List[int]) -> int:
            n = len(heights)

            if n == 0:
                return 0

            left_boundaries = [-1] * n
            right_boundaries = [n] * n

            stack = []

            for i, current_height in enumerate(heights):

                while stack and heights[stack[-1]] >= current_height:
                    stack.pop()

                if stack:
                    left_boundaries[i] = stack[-1]

                stack.append(i)

            stack = []

            for i in range(n - 1, -1, -1):

                current_height = heights[i]

                while stack and heights[stack[-1]] >= current_height:
                    stack.pop()

                if stack:
                    right_boundaries[i] = stack[-1]

                stack.append(i)

            # Calculate Maximum Area
            max_area = 0

            for i in range(n):
                width = right_boundaries[i] - left_boundaries[i] - 1
                area = heights[i] * width
                max_area = max(max_area, area)

            return max_area

        if not matrix or not matrix[0]:
            return 0

        num_cols = len(matrix[0])

        heights = [0] * num_cols

        max_area = 0

        # Build histogram row by row
        for row in matrix:

            for col_idx, value in enumerate(row):

                if value == "1":
                    heights[col_idx] += 1
                else:
                    heights[col_idx] = 0

            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
