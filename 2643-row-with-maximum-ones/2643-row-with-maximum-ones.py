class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0,0]

        for row_idx , row in enumerate(mat):
            ones_count = sum(row)
            if res[1] < ones_count:
                res = [row_idx , ones_count]
        return res