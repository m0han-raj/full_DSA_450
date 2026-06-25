class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for i in s:
            freq[i] =freq.get(i,0)+1
        for i in freq:
            if freq[i]==1:
                return s.index(i)
        return -1