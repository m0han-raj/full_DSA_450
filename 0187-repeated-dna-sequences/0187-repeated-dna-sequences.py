class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counters = Counter()
        result = []

        for i in range(len(s)-9):
            current_sequence = s[i:i+10]
            counters[current_sequence] +=1

            if counters[current_sequence]==2:
                result.append(current_sequence)

        return result