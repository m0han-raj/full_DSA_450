class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)

        for ch in t:
            count[ch]-=1
            if count[ch]<0:
                return ch
                