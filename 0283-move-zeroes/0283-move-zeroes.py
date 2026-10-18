class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for idx , right in enumerate(nums):
            if right !=0:
                nums[left] , nums[idx] = nums[idx] , nums[left]
                left+=1
        return nums
        