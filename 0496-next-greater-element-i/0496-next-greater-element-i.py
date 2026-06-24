class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk =[]
        mp = {}

        for num in nums2: #calculate the greater value elements
            while stk and num > stk[-1]:
                mp[stk.pop()] = num
            stk.append(num)

        while stk: #calculate the -1 
            mp[stk.pop()] = -1

        return [mp[num] for num in nums1]