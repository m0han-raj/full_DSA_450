class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr=nums

        pivot = -1 # step 1 find reverse
        for i in range(n-2,-1,-1): #n-2 to avoid list index errors , and iterate from the right
            if arr[i] < arr[i+1]:
                pivot=i
                break
        if pivot==-1:
            arr.reverse()
            return

        #step 2 find the smallest largest element and swap
        for i in range(n-1,pivot,-1): # swapping the smallest largest element with the pivot 
            if arr[i]>arr[pivot]:
                arr[i] , arr[pivot] = arr[pivot] , arr[i]
                break

        #step 3: reverse the right part after the pivot
        left , right = pivot+1 , n-1
        while left<right:
            arr[left] , arr[right] =arr[right] , arr[left]
            left+=1
            right-=1
        
        return arr
            