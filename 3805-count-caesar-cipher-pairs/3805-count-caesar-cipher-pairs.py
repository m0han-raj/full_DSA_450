class Solution:
    def countPairs(self, words: List[str]) -> int:
        freq=defaultdict(int)
        pairs=0

        for word in words:
            shift = ord(word[0])-ord('a')
            normalized = []

            for ch in word:
                normalized.append(
                    chr((ord(ch) -ord('a') - shift)%26 + ord('a'))
                )

            key = "".join(normalized)

            pairs += freq[key]
            freq[key]+=1
        return pairs