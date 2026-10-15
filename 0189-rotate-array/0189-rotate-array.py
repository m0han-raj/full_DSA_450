class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def rotate(arr,left,right):
            while left<right:
                arr[left] , arr[right] = arr[right] , arr[left]
                left+=1
                right-=1
            return arr
        
        k = k%n
        rotate(nums,0,n-1)
        rotate(nums,0,k-1)
        rotate(nums,k,n-1)
        