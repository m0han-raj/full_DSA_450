class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):

            # If current number is negative, swap max and min
            if nums[i] < 0:
                currMax, currMin = currMin, currMax # soul of the code here

            currMax = max(nums[i], currMax * nums[i])
            currMin = min(nums[i], currMin * nums[i])

            res = max(res, currMax)

        return res