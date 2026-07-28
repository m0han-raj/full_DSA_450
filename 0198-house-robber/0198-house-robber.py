from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(index:int):
            if index >=len(nums) :
                return 0

            rob_current = nums[index] + dfs(index+2)
            skip_current = dfs(index+1)


            return max(rob_current,skip_current)

        return dfs(0)