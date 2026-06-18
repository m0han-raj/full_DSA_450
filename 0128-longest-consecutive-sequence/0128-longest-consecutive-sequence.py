class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()
        res=0

        for i in nums:
            st.add(i)
        
        for val in st:

            if (val-1) not in st:
                curr = val
                count=0
                while curr in st:
                    curr+=1
                    count+=1
            
                res = max(res,count)
        return res