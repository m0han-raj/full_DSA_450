class Solution:
    def myAtoi(self, s: str) -> int:

        if not s:
            return 0
            
        n = len(s)
        index = 0

        while index < n and s[index] == " ":
            index+=1
        
        if index==n:
            return 0

        sign = -1 if s[index]=="-" else 1

        if s[index] in ["-","+"]:
            index+=1

        result = 0

        over_threshold = (2**31-1)//10

        while index < n :

            if not s[index].isdigit():
                break

            current_index = int(s[index])
            while result > over_threshold or (result==over_threshold and current_index>7):
                return 2**31-1 if sign > 0 else -(2**31)

            result = result*10 + current_index
            index+=1
        return sign*result