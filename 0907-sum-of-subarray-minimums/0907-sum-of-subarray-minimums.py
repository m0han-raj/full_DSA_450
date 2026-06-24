class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans=0
        left = [0]*n
        right = [0]*n

        stk =[]
        for i in range(n):#previous smaller element
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()

            if not stk:
                left[i] = i+1
            else:
                left[i] = i-stk[-1]
            stk.append(i)
        stk=[]
        for i in range(n-1,-1,-1): #next smaller element
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            if not stk :
                right[i] = n-i
            else:
                right[i] = stk[-1] - i
            stk.append(i)

        for i in range(n):
            ans += arr[i]*left[i]*right[i]
        return ans % (10**9+7)

            