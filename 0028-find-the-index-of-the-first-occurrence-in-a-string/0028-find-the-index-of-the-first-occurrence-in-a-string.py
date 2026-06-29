class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == " ":
            return 0

        haystack_len=len(haystack)
        needle_len = len(needle)

        if needle_len > haystack_len:
            return -1

        for start in range(haystack_len-needle_len+1):
            if haystack[start:start+ needle_len] == needle:
                return start

        return -1