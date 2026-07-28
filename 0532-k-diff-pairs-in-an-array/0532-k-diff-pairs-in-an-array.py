class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        unique_num = set()
        seen = set()

        for curr in nums:
            if curr-k in seen:
                unique_num.add(curr-k)

            if curr+k in seen:
                unique_num.add(curr)

            seen.add(curr)
        
        return len(unique_num)