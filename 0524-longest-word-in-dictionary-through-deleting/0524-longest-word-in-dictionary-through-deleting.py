class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_sequence(word,source):

            word_len , source_len = len(word) , len(source)
            word_idx =source_idx =0

            while word_idx < word_len and source_idx<source_len:
                if word[word_idx]==source[source_idx]:
                    word_idx+=1
                source_idx+=1
            return word_idx == word_len

        ans = ""

        for word in dictionary:
            if is_sequence(word,s):
                if len(ans) < len(word) or (len(ans)==len(word) and word < ans):
                    ans = word

        return ans

                