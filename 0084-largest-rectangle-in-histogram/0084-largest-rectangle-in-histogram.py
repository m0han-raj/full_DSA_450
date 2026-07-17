class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        left_boundaries =[-1]*n
        right_boundaries = [n]*n

        for i , current_index in enumerate(heights):
            while stack and heights[stack[-1]] >= current_index :
                right_boundaries[stack[-1]]=i
                stack.pop()
            
            if stack : 
                left_boundaries[i] = stack[-1]

            stack.append(i)
            
        max_area = 0

        for i,height in enumerate(heights):
            width = right_boundaries[i] - left_boundaries[i] -1
            area = width*height
            max_area = max(max_area , area)

        return max_area