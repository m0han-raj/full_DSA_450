class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last={char:index for index,char in enumerate(s)}

        stack =[]

        seen =set()

        for index,char in enumerate(s):

            if char in seen:
                continue

            while stack and stack[-1] > char and last[stack[-1]] > index:
                removed_char = stack.pop()
                seen.remove(removed_char)

            stack.append(char)
            seen.add(char)
        
        return "".join(stack)