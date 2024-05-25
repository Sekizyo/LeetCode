class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if not ch in word:
            return word

        endIndex = word.index(ch)
        pre = word[0:endIndex+1]
        post = word[endIndex+1:]
        return pre[::-1] + post
        