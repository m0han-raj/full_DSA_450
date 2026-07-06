class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digit = list(str(n))
        length = len(digit)

        pivot_idx = length -2
        while pivot_idx >=0 and digit[pivot_idx] >= digit[pivot_idx+1]:
            pivot_idx-=1

        if pivot_idx < 0:
            return -1

        swap_idx = length - 1
        while swap_idx >=0 and digit[pivot_idx]>=digit[swap_idx]:
            swap_idx -=1

        digit[swap_idx] , digit[pivot_idx] = digit[pivot_idx] , digit[swap_idx]

        digit[pivot_idx+1:] = digit[pivot_idx+1:][::-1]

        res = int(''.join(digit))

        return -1 if res > 2**31-1 else res
        