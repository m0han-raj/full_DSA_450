class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(s,left,right):
            while left < right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        left = 0
        right = len(s)-1

        while left < right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return (
                    ispalindrome(s,left+1,right) or
                    ispalindrome(s,left,right-1)
                )
        return True
                