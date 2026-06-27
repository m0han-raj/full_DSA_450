class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        digit_order =[
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]

        ans = [""]

        for digit in digits:
            letters = digit_order[int(digit)-2]

            ans = [existing + letter
            for existing in ans
            for letter in letters]

        return ans