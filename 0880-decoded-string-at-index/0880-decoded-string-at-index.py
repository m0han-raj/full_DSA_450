class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0

        for ch in s:
            if ch.isdigit():
                size*=int(ch)
            else:
                size+=1
        
        for i in range(len(s)-1,-1,-1):
            ch = s[i]

            k%=size

            if k==0 and ch.isalpha():
                return ch

            if ch.isdigit():
                size//=int(ch)
            else:
                size-=1