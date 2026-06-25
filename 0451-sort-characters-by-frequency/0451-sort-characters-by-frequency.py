class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        count = sorted(count.items(),key=lambda item:-item[1])

        return "".join(char*freq for char,freq in count)

        