class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0

        for i in s:
            if i == "(":
                current_depth+=1
                max_depth = max(max_depth,current_depth)
            elif i ==")":
                current_depth-=1
        return max_depth