class Solution:
    def isValid(self, s: str) -> bool:
        check_dict = {'}':"{" , "]" : "[" , ")" : "("}
        stk =[]

        for ch in s:
            if ch in "{([":
                stk.append(ch)
            else:
                if not stk or stk[-1]!=check_dict[ch]:
                    return False
                stk.pop()
        return len(stk)==0